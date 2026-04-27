import slugify from "slugify";
import { Category } from "../models/index.js";

const listCategories = async () => {
  const rows = await Category.findAll({ order: [["name", "ASC"]] });
  return { status: 200, body: rows };
};

const createCategory = async (nameInput) => {
  const name = nameInput?.trim();
  if (!name) return { status: 400, body: { detail: "Name is required." } };
  const category = await Category.create({ name, slug: slugify(name, { lower: true, strict: true }) });
  return { status: 201, body: category };
};

export { listCategories, createCategory };
