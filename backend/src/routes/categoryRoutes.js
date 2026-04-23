const router = require("express").Router();
const categoryController = require("../controllers/categoryController");
const { createCategoryBody } = require("../validators/categoryValidators");
const validate = require("../middlewares/validate");
const { requireAuth, requireAdmin } = require("../middlewares/auth");

router.get("/", categoryController.listCategories);
router.post("/", requireAuth, requireAdmin, validate({ body: createCategoryBody }), categoryController.createCategory);

module.exports = router;