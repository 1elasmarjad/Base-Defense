import pygame
import random


class DamageText:
    texts = []

    @classmethod
    # adds a text to list of fade
    def add(cls, font, display, string_text, x, y):
        text_obj = TextFadeOut(font, display, string_text, x, y, 200, 30, 30)
        cls.texts.append(text_obj)

    @classmethod
    def draw_all(cls, display, font):
        try:
            for i in range(len(cls.texts)):
                cls.texts[i].draw(font, display)
        except IndexError:
            None

    @classmethod
    def remove(cls, obj):
        cls.texts.remove(obj)


class TextFadeOut:
    __FADE_AWAY_TIME = 2  # higher the faster, smaller the slower

    def __init__(self, font, display, string_text, x, y, r, g, b):
        self.string_text = string_text
        self.font = font
        self.display = display
        self.x = x
        self.y = y
        self.text = font.render(str(self.string_text), False, (r, g, b))
        self.alpha_val = 255
        self.done = False

    def draw(self, font, display):
        if self.alpha_val > 0:
            self.alpha_val -= self.__FADE_AWAY_TIME
            self.text.set_alpha(self.alpha_val)
            display.blit(self.text, (self.x, self.y))
        else:
            self.done = True
            DamageText.remove(self)
            del self
