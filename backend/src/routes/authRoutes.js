const router = require('express').Router()
const authController = require("../controllers/authController");
const authValidators = require("../validators/authValidators");
const { requireAuth } = require("../middlewares/auth");
const validate = require("../middlewares/validate");

router.post("/login/", validate({ body: authValidators.loginBody }), authController.login);
router.post("/register/", validate({ body: authValidators.registerBody }), authController.register);
router.post("/reset/", validate({ body: authValidators.resetBody }), authController.resetPassword);
router.post("/verify/", validate({ body: authValidators.verificationBody }), authController.verifyEmail);
router.post("/refresh/", validate({ body: authValidators.refreshBody }), authController.refreshToken);
router.get("/profile/me/", requireAuth, authController.me);
router.patch("/profile/me/", requireAuth, validate({ body: authValidators.updateProfileBody }), authController.updateMe);
router.get("/poets/", authController.listPoets);

module.exports = router;