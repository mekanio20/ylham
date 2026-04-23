const router = require("express").Router();
const poemController = require("../controllers/poemController");
const poemValidators = require("../validators/poemValidators");
const { requireAuth, requireNotBanned } = require("../middlewares/auth");
const validate = require("../middlewares/validate");

router.get("/", validate({ query: poemValidators.listPoemsQuery }), poemController.listPoems);
router.post("/create", requireAuth, requireNotBanned, validate({ body: poemValidators.createPoemBody }), poemController.createPoem);
router.get("/:id", validate({ params: poemValidators.poemIdParam }), poemController.getPoem);

module.exports = router;