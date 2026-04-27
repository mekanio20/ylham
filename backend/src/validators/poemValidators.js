import Joi from 'joi'

const poemIdParam = Joi.object({
  id: Joi.number().integer().positive().required(),
});

const listPoemsQuery = Joi.object({
  q: Joi.string().allow(""),
});

const createPoemBody = Joi.object({
  title: Joi.string().min(1).max(255).required(),
  content: Joi.string().min(1).required(),
  tags: Joi.array().items(Joi.string().max(50)).max(10).default([]),
  backgroundImage: Joi.string().default("none"),
  backgroundMusic: Joi.string().default("none"),
  poemNote: Joi.string().allow(""),
  commentPermission: Joi.boolean().default(true),
  visibility: Joi.string().valid("public", "followers", "private").default("public"),
  isDraft: Joi.boolean().default(false),
  categoryId: Joi.number().integer().positive().allow(null),
});

export { poemIdParam, listPoemsQuery, createPoemBody };

export default { poemIdParam, listPoemsQuery, createPoemBody };
