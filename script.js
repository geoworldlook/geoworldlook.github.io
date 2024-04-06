
document.addEventListener('DOMContentLoaded', () => {
    // Funkcja do obsługi zmiany aktywnych zakładek i zawartości
    function handleTabChange(tabGroup, contentGroup, activeClass = 'active') {
        tabGroup.forEach(tab => {
            tab.addEventListener('click', () => {
                const targetId = tab.getAttribute('data-target');
                const targetContent = document.getElementById(targetId);
                
                contentGroup.forEach(c => c.classList.remove(activeClass));
                tabGroup.forEach(t => t.classList.remove(activeClass));
                
                tab.classList.add(activeClass);
                targetContent.classList.add(activeClass);
            });
        });
    }
    
    const tabs = document.querySelectorAll('.tab');
    const contents = document.querySelectorAll('.content');
    handleTabChange(tabs, contents);
    
    // Dla sub-tabów
    const subTabs = document.querySelectorAll('.sub-tab');
    const subContents = document.querySelectorAll('.sub-content');
    handleTabChange(subTabs, subContents);
});
