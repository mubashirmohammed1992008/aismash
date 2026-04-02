import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vite.dev/config/
export default defineConfig({
  plugins: [react()],
  server: {
    // Return index.html for all routes so React Router handles them,
    // including deep paths like /https://amazon.in/...
    historyApiFallback: {
      disableDotRule: true,  // don't treat dots in URLs as file extensions
      rewrites: [
        { from: /.*/, to: '/index.html' }
      ]
    }
  }
})

