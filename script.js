// Plik: script.js
document.addEventListener('DOMContentLoaded', () => {
    const toggleTheme = document.querySelector('.toggle-theme');
    const currentTheme = localStorage.getItem('theme') ? localStorage.getItem('theme') : null;

    if (currentTheme) {
        document.documentElement.setAttribute('data-theme', currentTheme);

        if (currentTheme === 'dark') {
            toggleTheme.textContent = 'Tryb jasny';
        }
    }

    toggleTheme.addEventListener('click', () => {
        let theme = document.documentElement.getAttribute('data-theme');
        let switchToTheme = theme === 'dark' ? 'light' : 'dark';
        document.documentElement.setAttribute('data-theme', switchToTheme);
        localStorage.setItem('theme', switchToTheme);
        toggleTheme.textContent = switchToTheme === 'dark' ? 'Tryb jasny' : 'Tryb ciemny';
    });
});
