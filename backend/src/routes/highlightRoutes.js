const router = require("express").Router();
const highlightController = require("../controllers/highlightController");
const { listHighlightsQuery } = require("../validators/highlightValidators");
const validate = require("../middlewares/validate");

router.get("/", validate({ query: listHighlightsQuery }), highlightController.listHighlights);
router.get("/top-poets", highlightController.topPoets);

module.exports = router;