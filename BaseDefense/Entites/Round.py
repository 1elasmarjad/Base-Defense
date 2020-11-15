class Round:
    round = 0
    enemies = 0

    @classmethod
    def go_to_next(cls):
        cls.round = cls.round + 1

    @property
    def round(cls):
        return cls.round

    @round.setter
    def round(cls, new):
        cls.round = new

    @classmethod
    def start_round(cls):
        if cls.round == 0:
            #SHOW STARTING MESSAGE:
            print("SHOW STARING MESSAGE")
        elif cls.round == 1:
            cls.generate_small_wooden_boats(5)

    # @classmethod
    # def generate_small_wooden_boats(cls, amnt):
    #     i = 1
    #     for i != amnt:
    #         []


