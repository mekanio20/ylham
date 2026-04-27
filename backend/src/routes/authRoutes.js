import { Router } from 'express';
import validate from '../middlewares/validate.js';
import authController from '../controllers/authController.js'
import authValidators from '../validators/authValidators.js'
import { requireAuth } from '../middlewares/auth.js'

const router = Router()

router.post("/login/", validate({ body: authValidators.loginBody }), authController.login);
router.post("/register/", validate({ body: authValidators.registerBody }), authController.register);
router.post("/reset/", validate({ body: authValidators.resetBody }), authController.resetPassword);
router.post("/verify/", validate({ body: authValidators.verificationBody }), authController.verifyEmail);
router.post("/refresh/", validate({ body: authValidators.refreshBody }), authController.refreshToken);
router.get("/profile/me/", requireAuth, authController.me);
router.patch("/profile/me/", requireAuth, validate({ body: authValidators.updateProfileBody }), authController.updateMe);
router.get("/poets/", authController.listPoets);

export default router