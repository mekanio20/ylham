const router = require("express").Router();
const interactionController = require("../controllers/interactionController");
const { requireAuth, requireNotBanned } = require("../middlewares/auth");
const validate = require("../middlewares/validate");
const interactionValidators = require("../validators/interactionValidators");

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

module.exports = router;