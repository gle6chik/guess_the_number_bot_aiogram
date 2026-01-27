// tailwind.config.js
export default {
    content: [
        './app/**/*.{js,ts,jsx,tsx,mdx}',
        // Важно: указать ВСЕ файлы, включая server components
    ],
    // В v4 нужно явно указать какие утилиты включать
    safelist: [
        'shadow-2xl',
        'hover:shadow-2xl',
        'shadow-md',
        'hover:shadow-md',
    ]
}