import pygame
import random


class CoinText:
    coin_texts = []

    @classmethod
    # adds a text to list of fade
    def add(cls, display, coins):
        cls.font = pygame.font.Font(pygame.font.get_default_font(), 28)
        text_obj = CoinFadeOut(cls.font, display, str(coins), cls.__random_x(), cls.__random_y(), True)
        cls.coin_texts.append(text_obj)

    @classmethod
    def add_less(cls, display, coins):
        cls.font = pygame.font.Font(pygame.font.get_default_font(), 28)
        text_obj = CoinFadeOut(cls.font, display, str(coins), cls.__random_x(), cls.__random_y(), False)
        cls.coin_texts.append(text_obj)

    @classmethod
    def __random_x(cls):
        return random.randint(860, 920)

    @classmethod
    def __random_y(cls):
        return random.randint(920, 970)

    @classmethod
    def draw_all(cls, display):
        try:
            for i in range(len(cls.coin_texts)):
                cls.coin_texts[i].draw(display)
        except IndexError:
            None

    @classmethod
    def remove(cls, obj):
        try:
            cls.texts.remove(obj)
        except AttributeError:
            None


class CoinFadeOut:
    __FADE_AWAY_TIME = 2  # higher the faster, smaller the slower

    def __init__(self, font, display, text, x, y, gained):
        self.text = text
        self.font = font
        self.display = display
        self.x = x
        self.y = y
        if gained:
            self.text = font.render(f"+{self.text}", False, (0, 200, 0))
        else:
            self.text = font.render(f"-{self.text}", False, (200, 0, 0))
        self.alpha_val = 255
        self.done = False

    def draw(self, display):
        if self.alpha_val > 0:
            self.alpha_val -= self.__FADE_AWAY_TIME
            self.text.set_alpha(self.alpha_val)
            display.blit(self.text, (self.x, self.y))
        else:
            self.done = True
            CoinText.remove(self)
            del self
