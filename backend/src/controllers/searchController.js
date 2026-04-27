import * as searchService from '../services/searchService.js'

export const searchPoems = async (req, res) => {
  const result = await searchService.searchPoems(req.query.q || "");
  return res.status(result.status).json(result.body);
};

export const searchPoets = async (req, res) => {
  const result = await searchService.searchPoets(req.query.q || "");
  return res.status(result.status).json(result.body);
};

export default { searchPoems, searchPoets };