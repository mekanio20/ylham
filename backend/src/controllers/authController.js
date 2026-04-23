const authService = require("../services/authService");

const login = async (req, res) => {
  const result = await authService.login(req.body);
  return res.status(result.status).json(result);
};

const register = async (req, res) => {
  const result = await authService.register(req.body);
  return res.status(result.status).json(result);
};

const resetPassword = async (req, res) => {
  const result = await authService.resetPassword(req.body);
  return res.status(result.status).json(result);
}

const verifyEmail = async (req, res) => {
  const result = await authService.verifyEmail(req.body);
  return res.status(result.status).json(result);
}

const refreshToken = async (req, res) => {
  const result = await authService.refreshToken(req.body);
  return res.status(result.status).json(result);
}

const me = async (req, res) => {
  const result = await authService.me(req.user.id);
  return res.status(result.status).json(result);
};

const updateMe = async (req, res) => {
  const result = await authService.updateMe(req.user.id, req.body);
  return res.status(result.status).json(result);
};

const listPoets = async (_req, res) => {
  const result = await authService.listPoets();
  return res.status(result.status).json(result);
};

module.exports = { login, register, resetPassword, verifyEmail, refreshToken, me, updateMe, listPoets };