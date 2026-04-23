const { Poem, PoemLike, Comment, CommentLike } = require("../models");
const Response = require("../utils/response");

const togglePoemLike = async (poemId, userId) => {
  const poem = await Poem.findByPk(poemId);
  if (!poem || poem.isDeleted) return Response.NotFound("Poem not found.");

  const existing = await PoemLike.findOne({ where: { poemId: poem.id, userId } });
  if (existing) {
    await existing.destroy();
    return Response.Success("Poem unliked successfully.", { liked: false });
  }
  await PoemLike.create({ poemId: poem.id, userId });
  return Response.Success("Poem liked successfully.", { liked: true });
};

const listComments = async (poemId) => {
  const rows = await Comment.findAll({ where: { poemId, isDeleted: false } });
  return Response.Success("Comments retrieved successfully.", { comments: rows });
};

const createComment = async (poemId, userId, content) => {
  const row = await Comment.create({ poemId, userId, content });
  return Response.Created("Comment created successfully.", { comment: row });
};

const toggleCommentLike = async (commentId, userId) => {
  const existing = await CommentLike.findOne({ where: { commentId, userId } });
  if (existing) {
    await existing.destroy();
    return Response.Success("Comment unliked successfully.", { liked: false });
  }
  await CommentLike.create({ commentId, userId });
  return Response.Success("Comment liked successfully.", { liked: true });
};

module.exports = { togglePoemLike, listComments, createComment, toggleCommentLike };
