import type { Config } from 'tailwindcss';

const config: Config = {
  content: ['./app/**/*.{js,ts,jsx,tsx,mdx}', './components/**/*.{js,ts,jsx,tsx,mdx}'],
  theme: {
    extend: {
      colors: {
        brand: {
          50: '#eefcff',
          500: '#0ea5e9',
          700: '#0369a1',
          900: '#0f172a',
        },
      },
    },
  },
  plugins: [],
};

export default config;
