import express, { NextFunction, Request, Response } from "express";
import { z } from "zod";

export function createServer() {
  // Create the app
  const app = express();
  app.use(express.json());

  // Example validation schema (unused in Hello World, for future use)
  const _helloSchema = z.object({
    name: z.string().min(1),
  });

  // Basic Hello World route
  app.get("/", (req: Request, res: Response) => {
    res.json({ message: "Hello, world!" });
  });

  // Health check
  app.get("/health", (req: Request, res: Response) => {
    res.json({ status: "ok" });
  });

  // Global error handler
  app.use((err: unknown, _req: Request, res: Response, _next: NextFunction) => {
    console.error("Unhandled error:", err);
    res.status(500).json({ error: "Internal Server Error" });
  });

  return app;
}