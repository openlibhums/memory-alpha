/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./content/**/*.html",
    "./themes/**/*.html",
    "./themes/**/*.js",
  ],
  theme: {
    container: {
      padding: {
        DEFAULT: '.5rem',
        sm: '3rem',
        lg: '6rem',
        xl: '8rem',
        '2xl': '10rem'
      }
    },
    colors: {
      black: '#31302b',
      white: '#fdfeff',
      tan: '#d6cbbc',
      orange: '#bb4e30',
      blue: '#36565f',
      rust: '#c08031',
      transparent: 'transparent',
      current: 'currentColor',
    },
    extend: {
      fontFamily: {
        poppins: ['Poppins Regular', 'sans-serif'],
        'poppins-medium': ['Poppins Medium', 'sans-serif'],
        'poppins-bold': ['Poppins Bold', 'sans-serif'],
        'space-mono': ['Space Mono Regular', 'sans-serif'],
        'space-mono-bold': ['Space Mono Bold', 'sans-serif'],
        'space-mono-italic': ['Space Mono Italic', 'sans-serif'],
        'space-mono-bold-italic': ['Space Mono Bold Italic', 'sans-serif'],
      },
    },
  },
  plugins: [],
}
