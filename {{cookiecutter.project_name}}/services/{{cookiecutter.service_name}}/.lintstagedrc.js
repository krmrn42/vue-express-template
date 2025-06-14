export default {
  "*.{ts,tsx,js}": ["pnpm format", "pnpm lint"],
  "*.{json,yml,yaml,md}": ["pnpm format"],
  "**/package.json": ["pnpm sort-package-json"],
};