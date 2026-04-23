require("dotenv").config();
const app = require("./app");
const port = process.env.PORT || 8001;
const { ensureDb } = require("./models");

const start = async () => {
  try {
    await ensureDb();
    app.listen(port, () => {
      console.log(`backend listening on ${port}`);
    });
  } catch (error) {
    console.error("Startup failed:", error.message);
    process.exit(1);
  }
};

start();
