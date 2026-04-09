/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx,vue}",
  ],
  theme: {
    extend: {
      fontFamily: {
        serif: ['Playfair Display', 'Georgia', 'serif'],
        sans: ['Inter', 'ui-sans-serif', 'system-ui', 'sans-serif'],
        garamond: ['Cormorant Garamond', 'Georgia', 'serif'],
        dm: ['DM Sans', 'sans-serif'],
      },
      colors: {
        paper: '#FDFCF8',
        muted: '#6B7280',
        border: '#E5E7EB',
      },
    },
  },
  plugins: [],
}
