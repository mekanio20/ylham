const { Op, Poem, User } = require("../models");
const Response = require("../utils/response");

const searchPoems = async (q = "") => {
  const rows = await Poem.findAll({
    where: {
      isDeleted: false,
      isDraft: false,
      approve: true,
      [Op.or]: [{ title: { [Op.iLike]: `%${q}%` } }, { content: { [Op.iLike]: `%${q}%` } }],
    },
    include: [{ model: User, as: "author", attributes: ["id", "username"] }],
    order: [["createdAt", "DESC"]],
  });
  return Response.Success("Poems retrieved successfully.", { poems: rows });
};

const searchPoets = async (q = "") => {
  const rows = await User.findAll({
    where: { username: { [Op.iLike]: `%${q}%` }, isBanned: false },
    attributes: ["id", "username", "createdAt"],
    order: [["username", "ASC"]],
  });
  return Response.Success("Poets retrieved successfully.", { poets: rows });
};

module.exports = { searchPoems, searchPoets };
