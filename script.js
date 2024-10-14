const organelles = {
    "Nucleus": "The control center of the cell that contains the cell's DNA and regulates gene expression.",
    "Mitochondria": "The powerhouse of the cell, producing energy (ATP) through cellular respiration.",
    "Ribosome": "Responsible for synthesizing proteins by translating RNA into proteins.",
    "Rough Endoplasmic Reticulum": "Covered with ribosomes and involved in the synthesis and modification of proteins.",
    "Smooth Endoplasmic Reticulum": "Involved in the synthesis of lipids and detoxification of harmful substances.",
    "Golgi Apparatus": "Modifies, sorts, and packages proteins and lipids for transport or storage.",
    "Lysosome": "Contains digestive enzymes that break down waste materials and cellular debris.",
    "Peroxisome": "Breaks down fatty acids and detoxifies harmful chemicals.",
    "Cytoskeleton": "Provides structural support and enables cell movement.",
    "Chloroplast": "Found in plant cells, responsible for converting sunlight into energy via photosynthesis.",
    "Cell Membrane": "A semipermeable barrier that controls what enters and leaves the cell.",
    "Vacuole": "Stores nutrients, waste products, and maintains turgor pressure in plant cells.",
    "Cell Wall": "Provides structural support and protection for plant cells.",
    "Centrosome": "Organizes microtubules and plays a key role in cell division."
};

// Get elements
const organelleList = document.getElementById('organelle-list');
const selectedOrganelle = document.getElementById('selected-organelle');

// Dynamically create the organelle list
Object.keys(organelles).forEach(organelle => {
    const li = document.createElement('li');
    li.textContent = organelle;
    organelleList.appendChild(li);
});

// Handle selection
let currentSelection = 0;
let listItems = organelleList.getElementsByTagName('li');

function updateSelection() {
    for (let i = 0; i < listItems.length; i++) {
        if (i === currentSelection) {
            listItems[i].classList.add('selected');
        } else {
            listItems[i].classList.remove('selected');
        }
    }
}

function showOrganelleDetails(organelle) {
    selectedOrganelle.innerHTML = `<h3>${organelle}</h3><p>${organelles[organelle]}</p>`;
}

// Initial selection update
updateSelection();

// Add keyboard navigation and selection logic
document.addEventListener('keydown', (e) => {
    if (e.key === 'ArrowUp' && currentSelection > 0) {
        currentSelection--;
    } else if (e.key === 'ArrowDown' && currentSelection < listItems.length - 1) {
        currentSelection++;
    } else if (e.key === 'Enter' || e.key === ' ') {
        const selected = listItems[currentSelection].textContent;
        showOrganelleDetails(selected);
    }
    updateSelection();
});

// Add click selection logic
Array.from(listItems).forEach((item, index) => {
    item.addEventListener('click', () => {
        currentSelection = index;
        const selected = listItems[currentSelection].textContent;
        showOrganelleDetails(selected);
        updateSelection();
    });
});
