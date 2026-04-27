import { Router } from 'express';
import validate from "../middlewares/validate.js";
import poemController from '../controllers/poemController.js'
import poemValidators from '../validators/poemValidators.js'
import { requireAuth, requireNotBanned } from '../middlewares/auth.js';

const router = Router()

router.get("/", validate({ query: poemValidators.listPoemsQuery }), poemController.listPoems);
router.post("/create", requireAuth, requireNotBanned, validate({ body: poemValidators.createPoemBody }), poemController.createPoem);
router.get("/:id", validate({ params: poemValidators.poemIdParam }), poemController.getPoem);

export default router