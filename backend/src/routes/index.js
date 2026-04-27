import { Router } from 'express';
import auth from './authRoutes.js'
import poems from './poemRoutes.js'
import categories from './categoryRoutes.js'
import interactions from './interactionRoutes.js'
import notifications from './notificationRoutes.js'
import highlights from './highlightRoutes.js'
import search from './searchRoutes.js'

const router = Router()

router.use("/auth", auth);
router.use("/poems", poems);
router.use("/categories", categories);
router.use("/notifications", notifications);
router.use("/highlights", highlights);
router.use("/search", search);
router.use("/", interactions);

export default router