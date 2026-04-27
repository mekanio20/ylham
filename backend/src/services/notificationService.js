import { Notification } from "../models/index.js";
import Response from "../utils/response.js";

const listNotifications = async (userId) => {
  const rows = await Notification.findAll({
    where: { recipientId: userId },
    order: [["createdAt", "DESC"]],
  });
  return Response.Success("Notifications retrieved successfully.", {
    notifications: rows,
  });
};

const unreadCount = async (userId) => {
  const count = await Notification.count({
    where: { recipientId: userId, isRead: false },
  });
  return Response.Success("Unread notification count retrieved successfully.", {
    unreadCount: count,
  });
};

const readAll = async (userId) => {
  await Notification.update(
    { isRead: true },
    { where: { recipientId: userId, isRead: false } },
  );
  return Response.Success("All notifications marked as read successfully.");
};

export { listNotifications, unreadCount, readAll };
