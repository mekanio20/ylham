import Joi from 'joi'

const poemIdParam = Joi.object({
  poemId: Joi.number().integer().positive().required(),
});

const commentIdParam = Joi.object({
  commentId: Joi.number().integer().positive().required(),
});

const createCommentBody = Joi.object({
  content: Joi.string().min(1).max(3000).required(),
});

export { poemIdParam, commentIdParam, createCommentBody };

export default { poemIdParam, commentIdParam, createCommentBody };
