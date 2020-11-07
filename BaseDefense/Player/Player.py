class Player:

    DEFAULT_COINS = 1000

    def __init__(self):
        self.coins = Player.DEFAULT_COINS
        self.alive = True
        self.inv = inventory()
