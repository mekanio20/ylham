const router = require("express").Router();
const notificationController = require("../controllers/notificationController");
const { requireAuth } = require("../middlewares/auth");

router.get("/", requireAuth, notificationController.listNotifications);
router.get("/unread-count", requireAuth, notificationController.unreadCount);
router.post("/read-all", requireAuth, notificationController.readAll);

module.exports = router;