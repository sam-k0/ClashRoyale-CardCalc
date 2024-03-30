document.addEventListener('DOMContentLoaded', function() {
    // Get the filter select element
    var filterSelect = document.getElementById('filter-select');

    // Get the card list container
    var cardList = document.getElementById('card-list');

    // Function to filter cards based on selected rarity
    function filterCards(rarity) {
        // Get all card items
        var cardItems = cardList.querySelectorAll('.card');

        // Loop through each card item
        cardItems.forEach(function(cardItem) {
            var cardRarity = cardItem.querySelector('.card-rarity').textContent.toLowerCase();

            console.log(cardRarity);
            // Show or hide card based on the selected rarity
            console.log("comparing " + rarity + " with " + cardRarity)

            if (rarity === 'all' || cardRarity === rarity) {
                console.log('show');
                cardItem.style.display = 'block'; // Show card
            } else {
                console.log('hide');
                cardItem.style.display = 'none'; // Hide card
            }
        });
    }

    // Add event listener to filter select
    filterSelect.addEventListener('change', function() {
        filterCards(this.value);
    });

    // Initial filter to display all cards
    filterCards('all');
});
