import { Router } from 'express';
import validate from '../middlewares/validate.js';
import interactionController from '../controllers/interactionController.js'
import interactionValidators from '../validators/interactionValidators.js'
import { requireAuth, requireNotBanned } from '../middlewares/auth.js';

const router = Router()

router.post(
  "/poems/:poemId/like",
  requireAuth,
  requireNotBanned,
  validate({ params: interactionValidators.poemIdParam }),
  interactionController.togglePoemLike,
);
router.get(
  "/poems/:poemId/comments",
  validate({ params: interactionValidators.poemIdParam }),
  interactionController.poemComments,
);
router.post(
  "/poems/:poemId/comments",
  requireAuth,
  requireNotBanned,
  validate({
    params: interactionValidators.poemIdParam,
    body: interactionValidators.createCommentBody,
  }),
  interactionController.poemComments,
);
router.post(
  "/comments/:commentId/like",
  requireAuth,
  requireNotBanned,
  validate({ params: interactionValidators.commentIdParam }),
  interactionController.toggleCommentLike,
);

export default router