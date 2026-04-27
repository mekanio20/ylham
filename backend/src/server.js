import dotenv from 'dotenv'
import app from './app.js'
import * as db from './models/index.js'
import { DB } from './models/index.js'
const port = process.env.PORT || 8001;
dotenv.config()
const models = [
  db.User,
  db.PoetProfile,
  db.EmailVerification,
  db.Category,
  db.Poem,
  db.PoemView,
  db.PoemLike,
  db.Comment,
  db.CommentLike,
  db.Notification,
  db.Highlight,
];

import AdminJS from "adminjs";
import AdminJSExpress from "@adminjs/express";
import AdminJSSequelize from "@adminjs/sequelize";

AdminJS.registerAdapter(AdminJSSequelize);

const admin = new AdminJS({
  rootPath: "/admin",
  resources: models,
});

const router = AdminJSExpress.buildAuthenticatedRouter(
  admin,
  {
    authenticate: async (email, password) => {
      if (email === process.env.ADMIN_EMAIL && password === process.env.ADMIN_PASSWORD) return { email };
      return null;
    },
    cookieName: process.env.ADMIN_PANEL_COOKIE_NAME,
    cookiePassword: process.env.ADMIN_PANEL_COOKIE_PASSWORD,
  }
);

app.use(admin.options.rootPath, router);

const start = async () => {
  try {
    app.listen(port, async () => {
      console.log(`AdminJS started on http://localhost:${port}${admin.options.rootPath}`);
      await DB.authenticate();
      await DB.sync({});
    });
  } catch (error) {
    console.error("Startup failed:", error.message);
    process.exit(1);
  }
};

start();