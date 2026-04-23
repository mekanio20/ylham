const express = require("express");
const cors = require("cors");
const morgan = require("morgan");
const apiRoutes = require("./routes");

const app = express();

app.use(cors({ origin: true, credentials: true }));
app.use(express.json({ limit: "2mb" }));
app.use(morgan("dev"));

app.get("/healthz", (_req, res) => res.json({ ok: true }));
app.use("/api", apiRoutes);

app.use((error, _req, res, _next) => {
  console.error(error);
  res.status(500).json({ detail: "Server error." });
});

module.exports = app;
