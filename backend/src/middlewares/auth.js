import jwt from 'jsonwebtoken'
import { User } from '../models/index.js'

export const requireAuth = async (req, res, next) => {
  try {
    const authHeader = req.headers["authorization"];
    const token = authHeader && authHeader.split(" ")[1];
    if (!token)
      return res.status(401).json({ detail: "Authentication required." });
    const decoded = jwt.verify(token, process.env.ACCESS_TOKEN_SECRET);
    console.log("AUTH DECODED --> ", decoded);
    req.user = decoded;
    return next();
  } catch (error) {
    return res.status(401).json({ detail: "Invalid or expired token." });
  }
};

export const requireAdmin = (req, res, next) => {
  if (!req.user?.isStaff)
    return res.status(403).json({ detail: "Admin only." });
  return next();
};

export const requireNotBanned = (req, res, next) => {
  if (req.user?.isBanned)
    return res.status(403).json({ detail: "User is banned." });
  return next();
};