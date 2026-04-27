import * as notificationService from '../services/notificationService.js'

export const listNotifications = async (req, res) => {
  const result = await notificationService.listNotifications(req.user.id);
  return res.status(result.status).json(result.body);
};

export const unreadCount = async (req, res) => {
  const result = await notificationService.unreadCount(req.user.id);
  return res.status(result.status).json(result.body);
};

export const readAll = async (req, res) => {
  const result = await notificationService.readAll(req.user.id);
  return res.status(result.status).json(result.body);
};

export default { listNotifications, unreadCount, readAll };