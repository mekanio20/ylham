import { Op, Poem, User, Category, PoemView } from '../models/index.js'
import Response from '../utils/response.js'

const poemIncludes = [
  { model: User, as: "author", attributes: ["id", "username"] },
  { model: Category, as: "category" },
];

const listPoems = async (q) => {
  const where = { isDeleted: false, isDraft: false, approve: true };
  if (q) {
    where[Op.or] = [
      { title: { [Op.iLike]: `%${q}%` } },
      { tags: { [Op.iLike]: `%${q}%` } },
    ];
  }
  const poems = await Poem.findAll({
    where,
    include: poemIncludes,
    order: [["createdAt", "DESC"]],
  });
  return Response.Success("Poems retrieved successfully.", { poems });
};

const createPoem = async (userId, payload) => {
  try {
    // if (payload.categoryId) {
    //   const category = await Category.findByPk(payload.categoryId);
    //   if (!category) throw new Error("Invalid category");
    // }
    const poem = await Poem.create({
      title: payload.title.trim(),
      content: payload.content,
      tags: payload.tags || "",
      backgroundImage: payload.backgroundImage || "none",
      backgroundMusic: payload.backgroundMusic || "none",
      poemNote: payload.poemNote || "",
      commentPermission: payload.commentPermission,
      visibility: payload.visibility || "public",
      isDraft: payload.isDraft,
      authorId: userId,
      categoryId: payload.categoryId || null,
    });
    return Response.Created("Poem created successfully.", { poem });
  } catch (error) {
    console.log('Name boldy ---> ', error);
    
    return Response.BadRequest(error.message || "Failed to create poem.");
  }
};

const getPoem = async ({ id, user, ip }) => {
  const poem = await Poem.findByPk(id, { include: poemIncludes });
  if (!poem || poem.isDeleted) return Response.NotFound("Poem not found.");
  if (poem.isDraft && poem.authorId !== user?.id && !user?.isStaff) {
    return Response.Unauthorized(
      "You do not have permission to view this poem.",
    );
  }

  const [_, created] = await PoemView.findOrCreate({
    where: { poemId: poem.id, userId: user?.id || null, ipAddress: ip || null },
    defaults: {
      poemId: poem.id,
      userId: user?.id || null,
      ipAddress: ip || null,
    },
  });
  if (created)
    await Poem.increment("viewCount", { by: 1, where: { id: poem.id } });

  return Response.Success("Poem retrieved successfully.", { poem });
};

export { listPoems, createPoem, getPoem };
