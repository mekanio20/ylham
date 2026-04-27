import Joi from 'joi'

const listHighlightsQuery = Joi.object({
  period: Joi.string().valid("daily", "weekly", "monthly", "yearly").default("weekly"),
});

export { listHighlightsQuery };
