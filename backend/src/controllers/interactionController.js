import * as interactionService from '../services/interactionService.js'

export const togglePoemLike = async (req, res) => {
  const result = await interactionService.togglePoemLike(req.params.poemId, req.user.id);
  return res.status(result.status).json(result.body);
};

export const poemComments = async (req, res) => {
  if (req.method === "GET") {
    const result = await interactionService.listComments(req.params.poemId);
    return res.status(result.status).json(result.body);
  }
  const result = await interactionService.createComment(req.params.poemId, req.user.id, req.body.content);
  return res.status(result.status).json(result.body);
};

export const toggleCommentLike = async (req, res) => {
  const result = await interactionService.toggleCommentLike(req.params.commentId, req.user.id);
  return res.status(result.status).json(result.body);
};

export default { togglePoemLike, poemComments, toggleCommentLike };