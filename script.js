// Sélectionne tous les boutons "Détails"
const buttons = document.querySelectorAll('.toggle-details');

// Fonction pour basculer la visibilité des détails
function toggleDetails(event) {
    const item = event.target.closest('.item');
    const details = item.querySelector('.details');

    if (details.style.display === 'none' || details.style.display === '') {
        details.style.display = 'block'; // Montrer les détails
    } else {
        details.style.display = 'none'; // Cacher les détails
    }
}

// Ajouter l'écouteur d'événements à chaque bouton
buttons.forEach(button => {
    button.addEventListener('click', toggleDetails);
});
