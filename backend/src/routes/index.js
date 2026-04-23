const router = require("express").Router();
const auth = require("./authRoutes");
const poems = require("./poemRoutes");
const categories = require("./categoryRoutes");
const interactions = require("./interactionRoutes");
const notifications = require("./notificationRoutes");
const highlights = require("./highlightRoutes");
const search = require("./searchRoutes");

router.use("/auth", auth);
router.use("/poems", poems);
router.use("/categories", categories);
router.use("/notifications", notifications);
router.use("/highlights", highlights);
router.use("/search", search);
router.use("/", interactions);

module.exports = router;