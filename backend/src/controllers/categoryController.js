const categoryService = require("../services/categoryService");

const listCategories = async (_req, res) => {
  const result = await categoryService.listCategories();
  return res.status(result.status).json(result.body);
};

const createCategory = async (req, res) => {
  const result = await categoryService.createCategory(req.body?.name);
  return res.status(result.status).json(result.body);
};

module.exports = { listCategories, createCategory };
