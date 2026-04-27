import express from 'express'
import cors from 'cors'
import morgan from 'morgan';
import apiRoutes from './routes/index.js'

const app = express();

app.use(cors({ origin: true, credentials: true }));
app.use(express.json({}));
app.use(morgan("dev"));

app.get("/healthz", (_req, res) => res.json({ ok: true }));
app.use("/api", apiRoutes);

app.use((error, _req, res, _next) => {
  console.error(error);
  res.status(500).json({ detail: "Server error." });
});

export default app;