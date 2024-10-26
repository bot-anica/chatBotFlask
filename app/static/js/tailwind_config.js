tailwind.config = {
  theme: {
    fontFamily: {
      sans: ['Graphik', 'sans-serif'],
      serif: ['Merriweather', 'serif'],
    },
    extend: {
      spacing: {
        '8xl': '96rem',
        '9xl': '128rem',
      },
      borderRadius: {
        '4xl': '2rem',
      },
      colors: {
        'blue-light': '#bcd8fa',
        'blue': '#0f67d1',
        'blue-dark': '#013c81',
        'purple-light': '#bdacfb',
        'purple': '#7a5ed5',
        'purple-dark': '#4b3293',
        'pink-light': '#fba9eb',
        'pink': '#ec6ed2',
        'pink-dark': '#aa238d',
        'red-light': '#ffb9b9',
        'red': '#d11c1c',
        'red-dark': '#730505',
        'orange-light': '#dc9277',
        'orange': '#dc6a41',
        'orange-dark': '#953a1a',
        'green-light': '#a7e6bc',
        'green': '#08c84d',
        'green-dark': '#02491a',
        'yellow-light': '#dfd674',
        'yellow': '#dfd02a',
        'yellow-dark': '#686102',
        'gray-dark': '#4e5c6e',
        'gray': '#8492a6',
        'gray-light': '#d3dce6',
        'gray-lightest': '#eff9ff',
      },
      keyframes: {
        fadeSlideIn: {
          '0%': { opacity: 0, transform: 'translateY(20px)' },
          '100%': { opacity: 1, transform: 'translateY(0)' },
        },
        slideDownFadeIn: {
          '0%': { opacity: 0, left: '50%', transform: 'translateX(-50%) translateY(-20px)' },
          '10%': { opacity: 1, left: '50%', transform: 'translateX(-50%) translateY(0)' },
          '90%': { opacity: 1, left: '50%', transform: 'translateX(-50%) translateY(0)' },
          '100%': { opacity: 0, left: '50%', transform: 'translateX(-50%) translateY(-20px)' },
        }
      }
    }
  }
}
