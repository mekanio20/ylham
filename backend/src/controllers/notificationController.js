const notificationService = require("../services/notificationService");

const listNotifications = async (req, res) => {
  const result = await notificationService.listNotifications(req.user.id);
  return res.status(result.status).json(result.body);
};

const unreadCount = async (req, res) => {
  const result = await notificationService.unreadCount(req.user.id);
  return res.status(result.status).json(result.body);
};

const readAll = async (req, res) => {
  const result = await notificationService.readAll(req.user.id);
  return res.status(result.status).json(result.body);
};

module.exports = { listNotifications, unreadCount, readAll };
