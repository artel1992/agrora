/** @type {import('tailwindcss').Config} */
module.exports = {
    content: [
        "./index.html",
        "./src/**/*.{vue,js,ts,jsx,tsx}",
    ],
    theme: {
        extend: {},
        namedGroup: ['home-page', 'slider']
    },
    // safelist: [
    //     {
    //         pattern: /.*?/,
    //     },
    // ],
    plugins: [
        require("tailwindcss-named-groups"),
    ],
}
