const base = require("../../eslint.config.cjs");

module.exports = [
  ...base.map((cfg) => {
    if (cfg.languageOptions?.parserOptions) {
      return {
        ...cfg,
        languageOptions: {
          ...cfg.languageOptions,
          parserOptions: {
            ...cfg.languageOptions.parserOptions,
            project: ["./tsconfig.vitest.json"],
          },
        },
      };
    }
    return cfg;
  }),
];