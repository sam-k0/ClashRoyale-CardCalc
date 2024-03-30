# Download all card images from the API
import requests
import RoyaleAPI

session = RoyaleAPI.Session()

player = session.get_player("PlayerTag")
card: RoyaleAPI.Card

for card in player.get_cards():
    # download card image
    with open("res/"+card.get("name")+".png", "wb") as f:
        f.write(requests.get(card.get("iconUrls")["medium"]).content)


