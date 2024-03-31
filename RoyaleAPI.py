import requests

PROXY_BASE = "https://proxy.royaleapi.dev"

COMMON_CARDS_UPGRADE_NUM = [1,2,4,10,20,50,100,200,400,800,1000,1500,3000,5000]
RARE_CARDS_UPGRADE_NUM =   [0,0,1,2,4,10,20,50,100,200,400,500,750,1250]
EPIC_CARDS_UPGRADE_NUM =   [0,0,0,0,0,1,2,4,10,20,40,50,100,200]
LEGENDARY_CARDS_UPGRADE_NUM = [0,0,0,0,0,0,0,0,1,2,4,6,10,20]
CHAMP_CARDS_UPGRADE_NUM = [0,0,0,0,0,0,0,0,0,0,1,2,8,20]

COMMON_CARDS_UPGRADE_COST = [0,5,20,50,150,400,1000,2000,4000,8000, 15000,35000, 75000, 100000]
RARE_CARDS_UPGRADE_COST =   [0,0,0,50,150,400,1000,2000,4000,8000, 15000,35000, 75000, 100000]
EPIC_CARDS_UPGRADE_COST =   [0,0,0,0,0,0,400,2000,4000,8000,15000,35000,75000,100000]
LEGENDARY_CARDS_UPGRADE_COST = [0,0,0,0,0,0,0,0,0,5000,15000,35000,75000, 100000]
CHAMP_CARDS_UPGRADE_COST = [0,0,0,0,0,0,0,0,0,0,0,35000,75000,100000]

RARITY_LEGENDARY = "legendary"
RARITY_EPIC = "epic"
RARITY_RARE = "rare"
RARITY_COMMON = "common"
RARITY_CHAMP = "champion"

class Card():
    def __init__(self, responseDict) -> None:
        self.data = responseDict
        self.name = responseDict.get("name")
        self.level = responseDict.get("level")
        self.starLevel = responseDict.get("starLevel")
        if self.starLevel == None:
            self.starLevel = 0
        self.maxLevel = responseDict.get("maxLevel")
        self.rarity = responseDict.get("rarity")
        self.count = responseDict.get("count")
        self.elixirCost = responseDict.get("elixirCost")
        self.iconUrls = responseDict.get("iconUrls")
        self.id = responseDict.get("id")
        self.imageUrls = responseDict.get("imageUrls")
        self.level_normalized = responseDict.get("level") + self.__get_rarity_level_offset()    
    def get(self, key: str) -> any:
        return self.data.get(key)

    def __get_rarity_level_offset(self):
        rarity = self.rarity
        rarityStart = 0
        if rarity == RARITY_COMMON:
            rarityStart = 0
        elif rarity == RARITY_RARE:
            rarityStart = 2
        elif rarity == RARITY_EPIC:
            rarityStart = 5
        elif rarity == RARITY_LEGENDARY:
            rarityStart = 8
        elif rarity == RARITY_CHAMP:
            rarityStart = 10
        else:
            raise ValueError("Invalid rarity")
        return rarityStart
        
    def __get_upgrade_cost_array(self)->list:
        rarity = self.rarity
        upgradeCost = []
        if rarity == RARITY_COMMON:
            upgradeCost = COMMON_CARDS_UPGRADE_COST
        elif rarity == RARITY_RARE:
            upgradeCost = RARE_CARDS_UPGRADE_COST
        elif rarity == RARITY_EPIC:
            upgradeCost = EPIC_CARDS_UPGRADE_COST
        elif rarity == RARITY_LEGENDARY:
            upgradeCost = LEGENDARY_CARDS_UPGRADE_COST
        elif rarity == RARITY_CHAMP:
            upgradeCost = CHAMP_CARDS_UPGRADE_COST
        else:
            raise ValueError("Invalid rarity")
        return upgradeCost
    
    def __get_upgrade_card_num_array(self)->list:
        upgradeNum = []
        rarity = self.rarity
        if rarity == RARITY_COMMON:
            upgradeNum = COMMON_CARDS_UPGRADE_NUM
        elif rarity == RARITY_RARE:
            upgradeNum = RARE_CARDS_UPGRADE_NUM
        elif rarity == RARITY_EPIC:
            upgradeNum = EPIC_CARDS_UPGRADE_NUM
        elif rarity == RARITY_LEGENDARY:
            upgradeNum = LEGENDARY_CARDS_UPGRADE_NUM
        elif rarity == RARITY_CHAMP:
            upgradeNum = CHAMP_CARDS_UPGRADE_NUM
        else:
            raise ValueError("Invalid rarity")
        return upgradeNum

    # methods to calculate missing cards until a certain level
    def get_required_upgrade_cards(self, currentLevel:int, targetLevel:int, currentCount:int, rarity:str) -> int:
        # Get the correct array of upgrade numbers
        if currentLevel >= targetLevel:
            return 0
        if targetLevel > 14:
            raise ValueError("Target level cannot be higher than 14, as it needs wildcard tokens to upgrade.")

        upgradeNum = []
        rarityStart = 0
        if rarity == RARITY_COMMON:
            upgradeNum = COMMON_CARDS_UPGRADE_NUM
        elif rarity == RARITY_RARE:
            upgradeNum = RARE_CARDS_UPGRADE_NUM
            rarityStart = 2
        elif rarity == RARITY_EPIC:
            upgradeNum = EPIC_CARDS_UPGRADE_NUM
            rarityStart = 5
        elif rarity == RARITY_LEGENDARY:
            rarityStart = 8
            upgradeNum = LEGENDARY_CARDS_UPGRADE_NUM
        elif rarity == RARITY_CHAMP:
            rarityStart = 10
            upgradeNum = CHAMP_CARDS_UPGRADE_NUM
        else:
            raise ValueError("Invalid rarity")
        
        # sum up the missing cards until the target level
        missingCards = 0
        for i in range(currentLevel+rarityStart, targetLevel):
            missingCards += upgradeNum[i]
        # factor in the current card count
        missingCards -= currentCount
        return missingCards
    
    def get_required_upgrade_cost(self, currentLevel:int, targetLevel:int, currentGold:int, rarity:str) -> int:
        # Get the correct array of upgrade numbers
        if currentLevel >= targetLevel:
            return 0
        if targetLevel > 14:
            raise ValueError("Target level cannot be higher than 14, as it needs wildcard tokens to upgrade.")

        upgradeCost = []
        rarityStart = 0
        if rarity == RARITY_COMMON:
            upgradeCost = COMMON_CARDS_UPGRADE_COST
        elif rarity == RARITY_RARE:
            upgradeCost = RARE_CARDS_UPGRADE_COST
            rarityStart = 2
        elif rarity == RARITY_EPIC:
            upgradeCost = EPIC_CARDS_UPGRADE_COST
            rarityStart = 5
        elif rarity == RARITY_LEGENDARY:
            rarityStart = 8
            upgradeCost = LEGENDARY_CARDS_UPGRADE_COST
        elif rarity == RARITY_CHAMP:
            rarityStart = 10
            upgradeCost = CHAMP_CARDS_UPGRADE_COST
        else:
            raise ValueError("Invalid rarity")
        
        # sum up the missing cards until the target level
        missingCost = 0
        for i in range(currentLevel+rarityStart, targetLevel):
            missingCost += upgradeCost[i]
        # factor in the current card count
        missingCost -= currentGold
        return missingCost

    def get_max_possible_upgrade_level(self):
        # calculate using information from the API,
        # as we have the current level and the count of the card and also the rarity
        rarityStart = self.__get_rarity_level_offset()
        upgradeCards = self.__get_upgrade_card_num_array()
        
        if self.level_normalized >= 14:
            return self.level_normalized, 0
        
        # calculate the max level
        maxLevel = 0
        totalCards = 0

        print("calculating ", self.name, self.level_normalized, self.count, self.rarity)
        # sum up all cards that are theoretically there due to the level
        for i in range(0, self.level_normalized):
            totalCards += upgradeCards[i]

        print(self.name , totalCards)
        # add the current cards
        totalCards += self.count
        
        # Subtract cards until < 0
        for i in range(0,14):
            totalCards -= upgradeCards[i]
            if totalCards < 0:
                break
            maxLevel += 1

        return maxLevel, abs(totalCards)
    



class Player():

    def __init__(self, responseDict) -> None:
        self.data = responseDict
        self.cards = []
        #serialize card list of dicts to Card objects
        for card in self.data.get("cards"):
            self.cards.append(Card(card))
    
    def get(self, key: str) -> any:
        return self.data.get(key)
    
    def get_cards(self) -> list:
        return self.cards
        

class Session():

    def __init__(self) -> None:
        with open("token.txt") as tk:
           self.token = tk.read()

    def get_player_raw(self, tag: str) -> dict:
        if tag.startswith("#"):
            tag = tag[1:]
        url = f"{PROXY_BASE}/v1/players/%23{tag}"
        headers = {"Authorization": f"Bearer {self.token}"}
        response = requests.get(url, headers=headers)
        return response.json()
        
    def get_player(self, tag: str) -> Player:
        get_player_raw = self.get_player_raw(tag)
        if "reason" in get_player_raw.keys():
            raise RuntimeError("Player not found")
        return Player(get_player_raw)