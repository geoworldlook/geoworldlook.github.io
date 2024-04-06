
document.addEventListener('DOMContentLoaded', () => {
    const tabs = document.querySelectorAll('.tab');
    const contents = document.querySelectorAll('.content');
    
    tabs.forEach(tab => {
        tab.addEventListener('click', () => {
            const targetId = tab.getAttribute('data-target');
            const targetContent = document.getElementById(targetId);
            
            contents.forEach(c => c.classList.remove('active'));
            targetContent.classList.add('active');
        });
    });

    // Dodaj tutaj logikę dla sub-tabów, jeśli potrzebujesz
});
