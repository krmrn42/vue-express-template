import request from "supertest";
import { describe, expect, it } from "vitest";
import { createServer } from "../src/server.js";

describe("GET /", () => {
  const app = createServer();

  it("responds with Hello", async () => {
    const res = await request(app).get("/");
    expect(res.status).toBe(200);
    expect(res.body.message).toBe("Hello, world!");
  });
});

describe("GET /health", () => {
  const app = createServer();

  it("responds with health status", async () => {
    const res = await request(app).get("/health");
    expect(res.status).toBe(200);
    expect(res.body.status).toBe("ok");
  });
});