import { Router } from 'express';
import notificationController from '../controllers/notificationController.js'
import { requireAuth } from '../middlewares/auth.js';

const router = Router()

router.get("/", requireAuth, notificationController.listNotifications);
router.get("/unread-count", requireAuth, notificationController.unreadCount);
router.post("/read-all", requireAuth, notificationController.readAll);

export default router