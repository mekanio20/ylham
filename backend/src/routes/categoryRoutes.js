import { Router } from 'express';
import validate from '../middlewares/validate.js';
import categoryController from '../controllers/categoryController.js'
import { createCategoryBody } from '../validators/categoryValidators.js'
import { requireAuth, requireAdmin } from '../middlewares/auth.js'

const router = Router()

router.get("/", categoryController.listCategories);
router.post("/", requireAuth, requireAdmin, validate({ body: createCategoryBody }), categoryController.createCategory);

export default router