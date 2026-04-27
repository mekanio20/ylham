const validate = ({ body, query, params }) => (req, res, next) => {
  const options = {
    abortEarly: false,
    stripUnknown: true,
  };

  if (body) {
    const { error, value } = body.validate(req.body, options);
    if (error) {
      return res.status(400).json({
        detail: "Validation error",
        errors: error.details.map((d) => d.message),
      });
    }
    req.body = value;
  }

  if (query) {
    const { error, value } = query.validate(req.query, options);
    if (error) {
      return res.status(400).json({
        detail: "Validation error",
        errors: error.details.map((d) => d.message),
      });
    }
    req.query = value;
  }

  if (params) {
    const { error, value } = params.validate(req.params, options);
    if (error) {
      return res.status(400).json({
        detail: "Validation error",
        errors: error.details.map((d) => d.message),
      });
    }
    req.params = value;
  }

  return next();
};

export default validate