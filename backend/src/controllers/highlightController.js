import * as highlightService from '../services/highlightService.js'

export const listHighlights = async (req, res) => {
  const result = await highlightService.listHighlights(req.query.period || "weekly");
  return res.status(result.status).json(result.body);
};

export const topPoets = async (req, res) => {
  const result = await highlightService.topPoets();
  return res.status(result.status).json(result.body);
};

export default { listHighlights, topPoets };