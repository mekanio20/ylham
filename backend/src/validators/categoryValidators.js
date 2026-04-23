const Joi = require("joi");

const createCategoryBody = Joi.object({
  name: Joi.string().trim().min(2).max(128).required(),
});

module.exports = { createCategoryBody };
