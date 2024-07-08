import globals from "globals"
import pluginJs from "@eslint/js"

export default [
  { ignores: ["build/", "src/websocket_relay.js"] },
  { languageOptions: { globals: globals.browser }},
  pluginJs.configs.recommended,
  {
    rules: {
      "no-unused-vars": [ "warn",
          { argsIgnorePattern: "^_", varsIgnorePattern: "^_" },
      ],
      "no-undef": "error",
      "no-empty": "warn",
    },
    languageOptions: {
      globals: {
        analytics:          "readonly",
        VIPER_IDE_VERSION:  "readonly",
        VIPER_IDE_BUILD:    "readonly",
      }
    }
  }
]
