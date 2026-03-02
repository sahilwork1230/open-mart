/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
// Target your specific app templates
    "./templates/**/*.html", 
    "./apps/**/templates/**/*.html", // If you have apps in an 'apps' folder
    "./static/**/*.js",
    // EXPLICITLY avoid venv and node_modules
  ],
  theme: {
    extend: {
      fontFamily: {
        'bogle': ['BBH Bogle', 'sans-serif'],
        'grover': ['Irish Grover', 'sans-serif'],
        'roboto': ['Roboto', 'sans-serif'],
        'iceland': ['Iceland', 'sans-serif'],
      },
      screens:{
        '3xl':'1600px',
      }
    },
  },
  plugins: [],
}