import vue from "@vitejs/plugin-vue";
import { defineConfig } from "vite";
import { fileURLToPath, URL } from "url";
import AutoImport from "unplugin-auto-import/vite";
import Components from "unplugin-vue-components/vite";
import vuetify from "vite-plugin-vuetify";

// https://vite.dev/config/
export default defineConfig({
  plugins: [
    vue(),
    AutoImport({
      imports: ["vue", "vue-router", "pinia"],
      dirs: [
        "src/components",
        "src/views",
        "src/layouts",
        "src/composables",
        "src/stores",
      ],
    }),
    Components({
      dirs: [
        "src/components",
        "src/views",
        "src/layouts",
        "src/composables",
        "src/stores",
      ],
      deep: true,
    }),
    vuetify({ autoImport: true }),
  ],
  resolve: {
    alias: [
      {
        find: "@",
        replacement: fileURLToPath(new URL("./src", import.meta.url)),
      },
    ],
  },
  build: {
    // Performance optimizations
    minify: "esbuild",
    rollupOptions: {
      output: {
        manualChunks: {
          vendor: ["vue", "vue-router", "vuetify"],
        },
      },
    },
    // Enable source maps for production debugging
    sourcemap: false,
    // Optimize chunk size
    chunkSizeWarningLimit: 1000,
  },
  // Development server optimizations
  server: {
    host: '0.0.0.0',
    hmr: {
      overlay: false,
    },
  },
  // CSS optimizations
  css: {
    devSourcemap: false,
  },
});
