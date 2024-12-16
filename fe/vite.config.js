import preact from '@preact/preset-vite';
import { defineConfig, loadEnv } from 'vite';

// https://vitejs.dev/config/
export default defineConfig(({ command, mode }) => {
  // Load env file based on `mode` in the current working directory.
  // Set the third parameter to '' to load all env regardless of the `VITE_` prefix.
  const env = loadEnv(mode, process.cwd(), '')
  
  return {
    plugins: [preact()],
    build: {
      outDir: 'dist',
      assetsDir: 'static',
      emptyOutDir: true,
    },
    server: {
      proxy: {
        '/api': 'http://localhost:8000',
      },
    },
    css: {
      postcss: './postcss.config.js',
    },
    define: {
      // Make env variables available globally
      'process.env': env
    },
  };
});
