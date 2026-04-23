const router = require("express").Router();
const searchController = require("../controllers/searchController");
const { searchQuery } = require("../validators/searchValidators");
const validate = require("../middlewares/validate");

router.get("/", validate({ query: searchQuery }), searchController.searchPoems);
router.get("/advanced", validate({ query: searchQuery }), searchController.searchPoems);
router.get("/poets", validate({ query: searchQuery }), searchController.searchPoets);

module.exports = router;