import { Op, Poem, User } from '../models/index.js'
import Response from '../utils/response.js'

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

export { searchPoems, searchPoets };
