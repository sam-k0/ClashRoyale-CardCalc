import RoyaleAPI as cr



session = cr.Session()

player = session.get_player("8JR9Y8YU")
card: cr.Card


for card in player.get_cards():
    print(card.starLevel)