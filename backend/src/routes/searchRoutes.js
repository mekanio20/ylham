import { Router } from 'express';
import validate from "../middlewares/validate.js";
import searchController from '../controllers/searchController.js'
import { searchQuery } from '../validators/searchValidators.js'

const router = Router()

router.get("/", validate({ query: searchQuery }), searchController.searchPoems);
router.get("/advanced", validate({ query: searchQuery }), searchController.searchPoems);
router.get("/poets", validate({ query: searchQuery }), searchController.searchPoets);

export default router