const searchService = require("../services/searchService");

const searchPoems = async (req, res) => {
  const result = await searchService.searchPoems(req.query.q || "");
  return res.status(result.status).json(result.body);
};

const searchPoets = async (req, res) => {
  const result = await searchService.searchPoets(req.query.q || "");
  return res.status(result.status).json(result.body);
};

module.exports = { searchPoems, searchPoets };
