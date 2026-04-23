const { Notification } = require("../models");
const Response = require("../utils/response");

const listNotifications = async (userId) => {
  const rows = await Notification.findAll({ where: { recipientId: userId }, order: [["createdAt", "DESC"]] });
  return Response.Success("Notifications retrieved successfully.", { notifications: rows });
};

const unreadCount = async (userId) => {
  const count = await Notification.count({ where: { recipientId: userId, isRead: false } });
  return Response.Success("Unread notification count retrieved successfully.", { unreadCount: count });
};

const readAll = async (userId) => {
  await Notification.update({ isRead: true }, { where: { recipientId: userId, isRead: false } });
  return Response.Success("All notifications marked as read successfully.");
};

module.exports = { listNotifications, unreadCount, readAll };
