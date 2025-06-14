export default {
  "*.{ts,tsx,js,vue}": ["prettier --write", "eslint --fix"],
  "*.{json,yml,yaml,md}": ["prettier --write"],
  "**/package.json": ["sort-package-json"],
};