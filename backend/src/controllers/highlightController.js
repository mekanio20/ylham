const highlightService = require("../services/highlightService");

const listHighlights = async (req, res) => {
  const result = await highlightService.listHighlights(req.query.period || "weekly");
  return res.status(result.status).json(result.body);
};

const topPoets = async (_req, res) => {
  const result = await highlightService.topPoets();
  return res.status(result.status).json(result.body);
};

module.exports = { listHighlights, topPoets };
