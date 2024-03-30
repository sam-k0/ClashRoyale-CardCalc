from flask import Flask, render_template, request
import RoyaleAPI as cr
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    user_input = request.form['user_input']
    targetlevel = request.form['targetlevel']
    

    session:cr.Session = cr.Session()
    player:cr.Player = session.get_player(user_input)
    cards:list = player.get_cards()
    cards_parsed = [] # conains a dict with the card name, rarity, level and count
    for card in cards:
        missingCards = card.get_required_upgrade_cards(card.get("level"), int(targetlevel), card.get("count"), card.get("rarity"))
        missingGold = card.get_required_upgrade_cost(card.get("level"), int(targetlevel), 0, card.get("rarity"))
        imgpath = "res/"+card.name+".png"
        
        cards_parsed.append(
            {"name":card.get("name"),
             "rarity":card.get("rarity"),
             "level":card.get("level"),
             "count":card.get("count"),
             "missingCards":missingCards,
             "missingGold":missingGold,
             "image_path": imgpath
             })

    return render_template('cards.html', cards=cards_parsed, targetlevel=targetlevel)



if __name__ == '__main__':
    app.run(debug=True)
