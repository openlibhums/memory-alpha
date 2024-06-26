/** @type {import('tailwindcss').Config} */

import typography from '@tailwindcss/typography'

// Algorithms from https://github.com/tailwindlabs/tailwindcss-typography/blob/master/src/styles.js
const round = (num) =>
  num
    .toFixed(7)
    .replace(/(\.[0-9]+?)0+$/, '$1')
    .replace(/\.0$/, '')
const rem = (px) => `${round(px / 16)}rem`
const em = (px, base) => `${round(px / base)}em`

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
      black: '#262522',
      white: '#fdfeff',
      tan: '#fdf3e3',
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
      // Customisation of Tailwind Typography plugin
      typography: ({ theme }) => ({
        DEFAULT: {
          css: {
            '--tw-prose-body': theme('colors.tan'),
            '--tw-prose-headings': theme('colors.tan'),
            '--tw-prose-links': theme('colors.tan'),
            '--tw-prose-bold': theme('colors.tan'),
            '--tw-prose-lead': theme('colors.tan'),
            '--tw-prose-bullets': theme('colors.tan'),
            '--tw-prose-hr': theme('colors.tan'),
            '--tw-prose-invert-body': theme('colors.blue'),
            '--tw-prose-invert-headings': theme('colors.blue'),
            '--tw-prose-invert-links': theme('colors.blue'),
            '--tw-prose-invert-bold': theme('colors.blue'),
            '--tw-prose-invert-lead': theme('colors.blue'),
            '--tw-prose-invert-bullets': theme('colors.blue'),
            '--tw-prose-invert-hr': theme('colors.blue'),
            p: {
              fontSize: rem(18),
              lineHeight: round(25 / 16),
              marginTop: em(12, 16),
              marginBottom: em(12, 16)
            },
            '[class~="lead"]': {
              fontFamily: 'Space Mono Regular',
              fontSize: em(24, 16),
              lineHeight: round(28 / 20)
            },
            h1: {
              fontFamily: 'Space Mono Regular',
              fontWeight: 'bold'
            },
            h2: {
              fontFamily: 'Space Mono Regular',
              fontWeight: 'bold'
            },
            h3: {
              fontFamily: 'Poppins Medium',
              fontWeight: 'bolder'
            }
          }
        },
        lg: {
          css: {
            '[class~="lead"]': {
              fontFamily: 'Space Mono Regular',
              fontSize: em(28, 18),
              lineHeight: round(26 / 20)
            },
            p: {
              fontSize: rem(20),
              lineHeight: round(26 / 18),
              marginTop: em(18, 18),
              marginBottom: em(18, 18)
            },
          }
        }
      }),
    },
  },
  plugins: [
    typography,
  ],
}
