const Joi = require("joi");

const poemIdParam = Joi.object({
  id: Joi.number().integer().positive().required(),
});

const listPoemsQuery = Joi.object({
  q: Joi.string().allow(""),
});

const createPoemBody = Joi.object({
  title: Joi.string().min(1).max(255).required(),
  content: Joi.string().min(1).required(),
  tags: Joi.string().allow(""),
  categoryId: Joi.number().integer().positive().allow(null),
  isDraft: Joi.boolean().default(false),
});

module.exports = { poemIdParam, listPoemsQuery, createPoemBody };
