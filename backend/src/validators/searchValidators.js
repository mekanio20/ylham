import Joi from 'joi'

const searchQuery = Joi.object({
  q: Joi.string().allow("").default(""),
});

export { searchQuery };
