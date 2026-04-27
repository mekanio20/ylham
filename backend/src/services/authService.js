import Response from "../utils/response.js";
import bcrypt from "bcryptjs";
import jwt from "jsonwebtoken";
import { User, EmailVerification, PoetProfile, DB } from "../models/index.js";
import { sendEmail } from "../utils/email.js";
import { generateTokens } from "../utils/tokens.js";
import { createUsername } from "../utils/username.js";
import { generateVerificationCode } from "../utils/otp.js";

class AuthService {
  login = async ({ email, password }) => {
    const user = await User.findOne({ where: { email, isActive: true } });
    if (!user || !(await bcrypt.compare(password, user.password))) {
      return Response.BadRequest("Invalid email or password.", {});
    }

    return Response.Success("Login successful.", {
      user: {
        id: user.id,
        email: user.email,
        username: user.username,
        isBanned: user.isBanned,
        isStaff: user.isStaff,
      },
      access: generateTokens(user).accessToken,
      refresh: generateTokens(user).refreshToken,
    });
  };

  register = async ({ email, password, termsAccepted }) => {
    try {
      const exists = await User.findOne({ where: { email } });
      if (exists)
        return Response.BadRequest(
          "A user with the same email or username already exists.",
          {},
        );
      const code = generateVerificationCode();
      const passwordHash = await bcrypt.hash(password, 10);
      const [verification, created] = await EmailVerification.findOrCreate({
        where: { email },
        defaults: {
          email,
          passwordHash,
          code,
          attempts: 1,
          expiresAt: new Date(Date.now() + 5 * 60 * 1000),
        },
      });
      if (!created) {
        verification.passwordHash = passwordHash;
        verification.code = code;
        verification.attempts += 1;
        verification.expiresAt = new Date(Date.now() + 5 * 60 * 1000);
        await verification.save();
      }
      await sendEmail(email, code);
      return Response.Created(
        "Verification code sent to email. Please verify to complete registration.",
        {},
      );
    } catch (error) {
      console.error("Registration error:", error);
      return Response.BadRequest("Registration failed.", {});
    }
  };

  resetPassword = async ({ email, password }) => {
    const user = await User.findOne({ where: { email } });
    if (!user)
      return Response.BadRequest("No user found with the provided email.", {});

    const code = generateVerificationCode();
    const passwordHash = await bcrypt.hash(password, 10);
    const [verification, created] = await EmailVerification.findOrCreate({
      where: { email },
      defaults: {
        email,
        passwordHash,
        code,
        attempts: 1,
        expiresAt: new Date(Date.now() + 5 * 60 * 1000),
      },
    });
    if (!created) {
      verification.passwordHash = passwordHash;
      verification.code = code;
      verification.attempts += 1;
      verification.expiresAt = new Date(Date.now() + 5 * 60 * 1000);
      await verification.save();
    }
    await sendEmail(email, code);

    return Response.Created("Send verification code.", {});
  };

  verifyEmail = async ({ email, code, purpose }) => {
    const verification = await EmailVerification.findOne({
      where: { email },
      order: [["createdAt", "DESC"]],
    });

    if (!verification || verification.code !== code)
      return Response.BadRequest("Invalid verification code.", {});
    if (verification.expiresAt < new Date())
      return Response.BadRequest("Verification code has expired.", {});

    const t = await DB.transaction();

    try {
      let user = {};

      if (purpose === "registration") {
        const username = await createUsername(email);
        [user] = await User.findOrCreate({
          where: { email: email },
          defaults: {
            email,
            username,
            password: verification.passwordHash,
            termsAccepted: true,
            isActive: true,
          },
          transaction: t,
        });
        if (user.id)
          await PoetProfile.create({ userId: user.id }, { transaction: t });
      } else {
        user = await User.findOne({ where: { email }, transaction: t });
        if (!user)
          return Response.BadRequest(
            "No user found with the provided email.",
            {},
          );
        user.password = verification.passwordHash;
        await user.save({ transaction: t });
      }

      await verification.destroy({ transaction: t });
      await t.commit();

      return Response.Success("Email verified successfully.", {
        user: {
          id: user?.id,
          email: user?.email,
          username: user?.username,
          isBanned: user?.isBanned,
          isStaff: user?.isStaff,
        },
        access: generateTokens(user).accessToken,
        refresh: generateTokens(user).refreshToken,
      });
    } catch (error) {
      console.error(error);
      await t.rollback();
      return Response.BadRequest("Error occurred.", error);
    }
  };

  refreshToken = async ({ refresh }) => {
    try {
      const payload = jwt.verify(refresh, process.env.REFRESH_TOKEN_SECRET);
      const user = await User.findByPk(payload.userId);
      if (!user || user.isBanned) {
        return Response.Unauthorized("Invalid refresh token.", {});
      }
      return Response.Success("Token refreshed successfully.", {
        user: {
          id: user.id,
          email: user.email,
          username: user.username,
          isBanned: user.isBanned,
          isStaff: user.isStaff,
        },
        access: generateTokens(user).accessToken,
        refresh: generateTokens(user).refreshToken,
      });
    } catch (error) {
      return Response.Unauthorized("Invalid refresh token.", {});
    }
  };

  me = async (userId) => {
    const user = await User.findByPk(userId);
    const profile = await PoetProfile.findOne({ where: { userId } });
    return Response.Success("User profile retrieved successfully.", {
      user,
      profile,
    });
  };

  updateMe = async (userId, payload) => {
    const profile = await PoetProfile.findOne({ where: { userId } });
    await profile.update(payload);
    return Response.Success("User profile updated successfully.", { profile });
  };

  listPoets = async () => {
    const poets = await PoetProfile.findAll({
      include: [
        { model: User, as: "user", attributes: ["id", "username", "isBanned"] },
      ],
      order: [["totalScore", "DESC"]],
    });
    return Response.Success("Poet profiles retrieved successfully.", { poets });
  };
}

export default new AuthService();