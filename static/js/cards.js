document.addEventListener('DOMContentLoaded', function() {
    // Get the filter select element
    var filterSelect = document.getElementById('filter-select');
    var searchInput = document.getElementById('search-text-filter');
    // Get the card list container
    var cardList = document.getElementById('card-list');

    // Function to filter cards based on selected rarity
    function filterCardsRarity(rarity) {
        // Get all card items
        var cardItems = cardList.querySelectorAll('.card');

        // Loop through each card item
        cardItems.forEach(function(cardItem) {
            var cardRarity = cardItem.querySelector('.card-rarity').textContent.toLowerCase();

            if (rarity === 'all' || cardRarity === rarity) {
                cardItem.style.display = 'flex'; // Show card
            } else {
                cardItem.style.display = 'none'; // Hide card
            }
        });
    }

    // search by text
    function filterCardsByName(name) {
        var cardItems = cardList.querySelectorAll('.card');
        name = name.toLowerCase(); // case insensitive search

        cardItems.forEach(function(cardItem) {
            var cardName = cardItem.querySelector('.card-name').textContent.toLowerCase();
            if (cardName.includes(name)) {
                cardItem.style.display = 'flex'; // Show card
            } else {
                cardItem.style.display = 'none'; // Hide card
            }

        });
    }

    // Add event listener to filter select
    filterSelect.addEventListener('change', function() {
        filterCardsRarity(this.value);
    });

    searchInput.addEventListener('keyup', function() {
        filterCardsByName(this.value);
    });

    // Initial filter to display all cards
    filterCardsRarity('all');

});
