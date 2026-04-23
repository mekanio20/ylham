const { literal } = require("sequelize");
const { Highlight, Poem, User } = require("../models");
const Response = require("../utils/response");

const listHighlights = async (period = "weekly") => {
  const rows = await Highlight.findAll({
    where: { period },
    include: [{ model: Poem, as: "poem", include: [{ model: User, as: "author", attributes: ["id", "username"] }] }],
    order: [["rank", "ASC"]],
  });
  return Response.Success("Highlights retrieved successfully.", { highlights: rows })
};

const topPoets = async () => {
  const rows = await Poem.findAll({
    where: { isDeleted: false, isDraft: false, approve: true },
    include: [{ model: User, as: "author", attributes: ["id", "username"] }],
    order: [[literal("\"Poem\".\"likeCount\" + \"Poem\".\"viewCount\""), "DESC"]],
    limit: 10,
  });
  return Response.Success("Top poets retrieved successfully.", { poems: rows })
};

module.exports = { listHighlights, topPoets };
