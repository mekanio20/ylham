const poemService = require("../services/poemService");

const listPoems = async (req, res) => {
  const result = await poemService.listPoems(req.query.q);
  return res.status(result.status).json(result.body);
};

const createPoem = async (req, res) => {
  const result = await poemService.createPoem(req.user.id, req.body);
  return res.status(result.status).json(result.body);
};

const getPoem = async (req, res) => {
  const result = await poemService.getPoem({ id: req.params.id, user: req.user, ip: req.ip });
  return res.status(result.status).json(result.body);
};

module.exports = { listPoems, createPoem, getPoem };
