import * as categoryService from '../services/categoryService.js'

export const listCategories = async (req, res) => {
  const result = await categoryService.listCategories();
  return res.status(result.status).json(result.body);
};

export const createCategory = async (req, res) => {
  const result = await categoryService.createCategory(req.body?.name);
  return res.status(result.status).json(result.body);
};

export default { listCategories, createCategory };