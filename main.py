import requests
import RoyaleAPI

session = RoyaleAPI.Session()

player = session.get_player("8JR9Y8YU")

# print all cards rarity and count
card: RoyaleAPI.Card


for card in player.get_cards():
    # calculate missing cards to level 14
    missingCards = card.get_required_upgrade_cards(card.get("level"), 14, card.get("count"), card.get("rarity"))
    missingGold = card.get_required_upgrade_cost(card.get("level"), 14, 0, card.get("rarity"))
    print(f"{card.name} ({card.rarity}): ({missingCards}, {missingGold} Gold missing to level 14)")

    # download card image
    print(card.iconUrls['medium'])
    response = requests.get(card.iconUrls['medium'])
    with open(f"res/{card.name}.png", "wb") as f:
        f.write(response.content)
        print(f"Downloaded {card.name}.png")

