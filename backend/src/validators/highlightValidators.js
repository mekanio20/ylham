const Joi = require("joi");

const listHighlightsQuery = Joi.object({
  period: Joi.string().valid("daily", "weekly", "monthly", "yearly").default("weekly"),
});

module.exports = { listHighlightsQuery };
