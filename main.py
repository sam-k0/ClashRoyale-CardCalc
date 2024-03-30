import requests
import RoyaleAPI

session = RoyaleAPI.Session()

player = session.get_player("8JR9Y8YU")

# print all cards rarity and count
card: RoyaleAPI.Card

for card in player.get_cards():
    # calculate missing cards to level 14
    if card.name == "Executioner":
        print(card.get_max_possible_upgrade_level())


