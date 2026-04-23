const Joi = require("joi");

const verificationBody = Joi.object({
  email: Joi.string().email().required(),
  code: Joi.string().length(6).required(),
  purpose: Joi.string().valid("registration", "password_reset").required(),
});

const resetBody = Joi.object({
  email: Joi.string().email().required(),
  password: Joi.string().min(6).max(128).required(),
});

const refreshBody = Joi.object({
  refresh: Joi.string().required(),
});

const registerBody = Joi.object({
  email: Joi.string().email().required(),
  password: Joi.string().min(6).max(128).required(),
  termsAccepted: Joi.boolean().valid(true).required(),
});

const loginBody = Joi.object({
  email: Joi.string().email().required(),
  password: Joi.string().min(1).required(),
});

const updateProfileBody = Joi.object({
  firstName: Joi.string().allow("", null).max(64),
  lastName: Joi.string().allow("", null).max(64),
  bio: Joi.string().allow("", null).max(5000),
  instagram: Joi.string().allow("", null).max(255),
  tiktok: Joi.string().allow("", null).max(255),
  imo: Joi.string().allow("", null).max(255),
}).min(1);

module.exports = { verificationBody, resetBody, refreshBody, registerBody, loginBody, updateProfileBody };
