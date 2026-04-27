import { DataTypes, Op, Sequelize } from "sequelize";
import { DB } from "../config/database.js";

const User = DB.define("User", {
  username: { type: DataTypes.STRING(50), allowNull: false, unique: true },
  email: { type: DataTypes.STRING(255), allowNull: false, unique: true },
  password: { type: DataTypes.STRING(255), allowNull: false },
  isActive: { type: DataTypes.BOOLEAN, defaultValue: false },
  isStaff: { type: DataTypes.BOOLEAN, defaultValue: false },
  isBanned: { type: DataTypes.BOOLEAN, defaultValue: false },
  termsAccepted: { type: DataTypes.BOOLEAN, defaultValue: false, allowNull: false },
});

const PoetProfile = DB.define("PoetProfile", {
  firstName: DataTypes.STRING(64),
  lastName: DataTypes.STRING(64),
  bio: DataTypes.TEXT,
  avatar: DataTypes.TEXT,
  instagram: DataTypes.STRING(255),
  tiktok: DataTypes.STRING(255),
  imo: DataTypes.STRING(255),
  totalScore: { type: DataTypes.INTEGER, defaultValue: 0 },
  isPrivate: { type: DataTypes.BOOLEAN, defaultValue: false },
});

const EmailVerification = DB.define("EmailVerification", {
  email: { type: DataTypes.STRING(255), unique: true },
  passwordHash: { type: DataTypes.STRING(255), allowNull: false },
  code: { type: DataTypes.STRING(6), allowNull: false },
  attempts: { type: DataTypes.INTEGER, defaultValue: 0 },
  isVerified: { type: DataTypes.BOOLEAN, defaultValue: false },
  expiresAt: { type: DataTypes.DATE, allowNull: false },
});

const Category = DB.define("Category", {
  name: { type: DataTypes.STRING(128), unique: true, allowNull: false },
  slug: { type: DataTypes.STRING(140), unique: true, allowNull: false },
});

const Poem = DB.define("Poem", {
  title: { type: DataTypes.STRING(255), allowNull: false },
  content: { type: DataTypes.TEXT, allowNull: false },
  tags: { type: DataTypes.ARRAY(DataTypes.STRING), defaultValue: [""] },
  backgroundImage: { type: DataTypes.STRING(64), defaultValue: "none" },
  backgroundMusic: { type: DataTypes.STRING(64), defaultValue: "none" },
  likeCount: { type: DataTypes.INTEGER, defaultValue: 0 },
  commentCount: { type: DataTypes.INTEGER, defaultValue: 0 },
  viewCount: { type: DataTypes.INTEGER, defaultValue: 0 },
  poemNote: { type: DataTypes.TEXT },
  commentPermission: { type: DataTypes.BOOLEAN, defaultValue: true },
  visibility: { type: DataTypes.ENUM("public", "followers", "private"), defaultValue: "public" },
  isDraft: { type: DataTypes.BOOLEAN, defaultValue: false },
  approve: { type: DataTypes.BOOLEAN, defaultValue: false },
  isDeleted: { type: DataTypes.BOOLEAN, defaultValue: false },
  deletedAt: { type: DataTypes.DATE },
});

const PoemView = DB.define("PoemView", {
  ipAddress: DataTypes.STRING(64),
  viewedAt: { type: DataTypes.DATE, defaultValue: DataTypes.NOW },
});

const PoemLike = DB.define("PoemLike", {});

const Comment = DB.define("Comment", {
  content: { type: DataTypes.TEXT, allowNull: false },
  likeCount: { type: DataTypes.INTEGER, defaultValue: 0 },
  isDeleted: { type: DataTypes.BOOLEAN, defaultValue: false },
  deletedAt: DataTypes.DATE,
});

const CommentLike = DB.define("CommentLike", {});

const Notification = DB.define("Notification", {
  notificationType: {
    type: DataTypes.ENUM("like", "comment", "follower", "system"),
    defaultValue: "system",
  },
  message: DataTypes.TEXT,
  isRead: { type: DataTypes.BOOLEAN, defaultValue: false },
});

const Highlight = DB.define("Highlight", {
  period: {
    type: DataTypes.ENUM("daily", "weekly", "monthly", "yearly"),
    allowNull: false,
  },
  rank: { type: DataTypes.INTEGER, allowNull: false },
  score: { type: DataTypes.INTEGER, defaultValue: 0 },
  isManual: { type: DataTypes.BOOLEAN, defaultValue: false },
});

User.hasOne(PoetProfile, { foreignKey: "userId", as: "profile", onDelete: "CASCADE" });
PoetProfile.belongsTo(User, { foreignKey: "userId", as: "user" });

User.hasMany(Poem, { foreignKey: "authorId", as: "poems" });
Poem.belongsTo(User, { foreignKey: "authorId", as: "author" });

Category.hasMany(Poem, { foreignKey: "categoryId", as: "poems" });
Poem.belongsTo(Category, { foreignKey: "categoryId", as: "category" });

Poem.hasMany(PoemView, { foreignKey: "poemId" });
PoemView.belongsTo(Poem, { foreignKey: "poemId" });
User.hasMany(PoemView, { foreignKey: "userId" });
PoemView.belongsTo(User, { foreignKey: "userId" });

User.belongsToMany(Poem, { through: PoemLike, as: "likedPoems", foreignKey: "userId" });
Poem.belongsToMany(User, { through: PoemLike, as: "likedBy", foreignKey: "poemId" });

User.hasMany(Comment, { foreignKey: "userId" });
Comment.belongsTo(User, { foreignKey: "userId", as: "user" });
Poem.hasMany(Comment, { foreignKey: "poemId" });
Comment.belongsTo(Poem, { foreignKey: "poemId", as: "poem" });

User.belongsToMany(Comment, { through: CommentLike, as: "likedComments", foreignKey: "userId" });
Comment.belongsToMany(User, { through: CommentLike, as: "likedBy", foreignKey: "commentId" });

User.hasMany(Notification, { foreignKey: "recipientId", as: "notifications" });
Notification.belongsTo(User, { foreignKey: "recipientId", as: "recipient" });
User.hasMany(Notification, { foreignKey: "senderId", as: "sentNotifications" });
Notification.belongsTo(User, { foreignKey: "senderId", as: "sender" });
Poem.hasMany(Notification, { foreignKey: "poemId" });
Notification.belongsTo(Poem, { foreignKey: "poemId", as: "poem" });

Poem.hasMany(Highlight, { foreignKey: "poemId" });
Highlight.belongsTo(Poem, { foreignKey: "poemId", as: "poem" });
User.hasMany(Highlight, { foreignKey: "selectedById", as: "selectedHighlights" });
Highlight.belongsTo(User, { foreignKey: "selectedById", as: "selectedBy" });

PoemLike.addHook("afterCreate", async (like) => {
  await Poem.increment("likeCount", { by: 1, where: { id: like.poemId } });
});
PoemLike.addHook("afterDestroy", async (like) => {
  await Poem.decrement("likeCount", { by: 1, where: { id: like.poemId } });
});

Comment.addHook("afterCreate", async (comment) => {
  await Poem.increment("commentCount", { by: 1, where: { id: comment.poemId } });
});
Comment.addHook("afterDestroy", async (comment) => {
  await Poem.decrement("commentCount", { by: 1, where: { id: comment.poemId } });
});

export {
  Op,
  DB,
  Sequelize,
  User,
  PoetProfile,
  EmailVerification,
  Category,
  Poem,
  PoemView,
  PoemLike,
  Comment,
  CommentLike,
  Notification,
  Highlight,
};