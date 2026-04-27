import { Router } from 'express';
import { listHighlightsQuery } from '../validators/highlightValidators.js'
import highlightController from "../controllers/highlightController.js"
import validate from "../middlewares/validate.js";

const router = Router()

router.get("/", validate({ query: listHighlightsQuery }), highlightController.listHighlights);
router.get("/top-poets", highlightController.topPoets);

export default router