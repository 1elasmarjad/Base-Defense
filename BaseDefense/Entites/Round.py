import pygame
from Entites import EnemyList, Enemy
import random
import os


class Round:
    rnd = 0
    round_ended = True
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(THIS_FOLDER, 'advance.png')
    advance = pygame.image.load(path)

    @classmethod
    def next_round(cls):
        cls.rnd += 1

    @property
    def round(cls):
        return cls.rnd

    @round.setter
    def round(cls, new):
        cls.round = new

    @classmethod
    def start_round(cls):
        cls.round_ended = False
        #  SHOW "ROUND x HAS BEGUN" text, add delay...
        if cls.rnd == 1:
            cls.generate_small_wooden_boats(2)
        elif cls.rnd == 2:
            cls.generate_small_wooden_boats(6)
        elif cls.rnd == 3:
            cls.generate_small_wooden_boats(8)

    @classmethod
    def check_round(cls, enms, display):
        counter_font = pygame.font.Font(pygame.font.get_default_font(), 30)

        if enms <= 0:
            cls.round_ended = True
            out = f"Round {cls.rnd + 1}..."
            advance_rect = cls.advance.get_rect(center=(960, 150))
            display.blit(cls.advance, advance_rect)  # displays scope
        else:
            cls.round_ended = False
            out = f"{enms} enemies remain"

        text = counter_font.render(str(out), False, (0, 0, 0))
        text_rect = text.get_rect(center=(960, 850))
        display.blit(text, text_rect)

    @classmethod
    def generate_small_wooden_boats(cls, amnt):
        for i in range(amnt):
            EnemyList.EnemyList.add(Enemy.SmallWoodenBoat(cls.__random_x(), cls.__random_y()))

    @classmethod
    def __random_x(cls):
        if random.randint(1, 2) == 1:
            # LEFT SIDE
            return random.randint(-500, -100)
        else:
            # RIGHT SIDE
            return random.randint(2020, 2720)

    @classmethod
    def __random_y(cls):
        return random.randint(64, 1016)
