const Joi = require("joi");

const searchQuery = Joi.object({
  q: Joi.string().allow("").default(""),
});

module.exports = { searchQuery };
