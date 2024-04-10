function changeLanguage(lang) {
  var textsToChange = document.querySelectorAll('[data-lang]');
  textsToChange.forEach(function(elem) {
    elem.textContent = translations[lang][elem.getAttribute('data-lang')];
  });
}

var translations = {
  'en': {
    'intro': 'Introduction to the project',
    'stage1': 'Stage 1: Selection of potential sites for photovoltaic farms',
    'stage2': 'Stage 2: Selection of potential sites for wind farms',
    'stage3': 'Stage 3: Solar radiation values for the selected areas',
    // continue for each piece of text you want to translate
  },
  'pl': {
    'intro': 'Wprowadzenie do projektu',
    'stage1': 'Etap 1: Selekcja potencjalnych miejsc pod farmy fotowoltaiczne',
    'stage2': 'Etap 2: Selekcja potencjalnych miejsc pod farmy wiatrowe',
    'stage3': 'Etap 3: Wartości promieniowania słonecznego dla wyselekcjonowanych obszarów',
    // the rest of your original Polish text goes here
  }
};




function changeTab(evt, tabName) {
    var i, tabcontent, tab;
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }
    tab = document.getElementsByClassName("tab");
    for (i = 0; i < tab.length; i++) {
        tab[i].className = tab[i].className.replace(" active", "");
    }
    document.getElementById(tabName).style.display = "block";
    evt.currentTarget.className += " active";
}

// Aktywuj pierwszą zakładkę domyślnie
window.onload = function() {
    document.getElementsByClassName("tab")[0].click();
};
