import jwt from 'jsonwebtoken';

export const generateTokens = (user) => {
  const accessToken = jwt.sign({ userId: user.id, isBanned: user.isBanned, isStaff: user.isStaff }, process.env.ACCESS_TOKEN_SECRET, { expiresIn: '15m' });
  const refreshToken = jwt.sign({ userId: user.id, isBanned: user.isBanned, isStaff: user.isStaff }, process.env.REFRESH_TOKEN_SECRET, { expiresIn: '30d' });
  return { accessToken, refreshToken };
};