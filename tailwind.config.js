/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./templates/*.{html,js}"],
  theme: {
    extend: {
      colors:{
        primary: "#122b39",
        letters: "#35b29c"
      },
      backgroundImage: {
        'home-page': "url('/static/logos/dentistaIndex.jpg')"                                     
      }
    },
  },
  plugins: [],
}
