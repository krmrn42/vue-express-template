const { defineConfig, globalIgnores } = require("eslint/config");

const globals = require("globals");
const tsParser = require("@typescript-eslint/parser");
const typescriptEslint = require("@typescript-eslint/eslint-plugin");
const vitest = require("@vitest/eslint-plugin");
const js = require("@eslint/js");

const { FlatCompat } = require("@eslint/eslintrc");

const compat = new FlatCompat({
  baseDirectory: __dirname,
  recommendedConfig: js.configs.recommended,
  allConfig: js.configs.all,
});

module.exports = defineConfig([
  {
    files: ["**/*.ts"],
    languageOptions: {
      parser: tsParser,
      parserOptions: {
        project: "./tsconfig.json",
      },
      sourceType: "module",
      ecmaVersion: "latest",
      globals: {
        ...globals.node,
      },
    },
    plugins: {
      "@typescript-eslint": typescriptEslint,
    },
    rules: {
      ...typescriptEslint.configs["recommended"].rules,
      ...typescriptEslint.configs["strict-type-checked"].rules,
      ...typescriptEslint.configs["stylistic"].rules,
      "@typescript-eslint/no-unused-vars": [
        "warn",
        { argsIgnorePattern: "^_" },
      ],
      "@typescript-eslint/restrict-template-expressions": [
        "error",
        {
          allowBoolean: true,
          allowNullish: true,
          allowRegExp: true,
          allowNumber: true,
        },
      ],
    },
  },
  {
    files: ["**/*.test.ts", "**/tests/**/*.ts", "**/__tests__/**/*.ts"],
    languageOptions: {
      parser: tsParser,
      parserOptions: {
        project: "./tsconfig.json",
      },
      sourceType: "module",
      ecmaVersion: "latest",
      globals: {
        ...globals.node,
        ...globals.vitest,
      },
    },
    plugins: {
      vitest,
    },
    rules: {
      "vitest/no-focused-tests": "error",
      "vitest/consistent-test-it": ["warn", { fn: "it" }],
      "@typescript-eslint/no-unused-vars": [
        "warn",
        { argsIgnorePattern: "^_" },
      ],
      "@typescript-eslint/no-unsafe-member-access": "off",
    },
  },
  globalIgnores(["**/dist/", "**/node_modules/", "**/coverage/", "**/*.d.ts"]),
]);