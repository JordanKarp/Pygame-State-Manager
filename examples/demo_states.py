import pygame as pg
from random import random


from state import State


class Game(State):
    def __init__(self):
        self.next_state = None
        self.persist = {}
        self.ball = Ball()

    def startup(self, persistent={}):
        """Upon state startup"""
        self.next_state = self
        self.persist = persistent

    def handle_event(self, event):
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                self.ball.rand_position()
            if event.key == pg.K_ESCAPE:
                self.next_state = "PAUSE"

    def update(self, dt):
        self.ball.update(dt)

    def draw(self, screen):
        """Draw state"""
        screen.fill((240, 240, 240))
        draw_text(
            screen,
            "Main Game! Space to move ball, Escape to pause (and switch states).",
        )
        self.ball.draw(screen)

    def cleanup(self):
        self.persist["ball"] = self.ball


class Pause(State):
    def __init__(self):
        self.next_state = None
        self.persist = {}

    def startup(self, persistent={}):
        """Upon state startup"""
        self.next_state = self
        self.persist = persistent
        self.ball = self.persist["ball"]

    def handle_event(self, event):
        if event.type == pg.KEYDOWN:
            self.next_state = None

    def update(self, dt):
        pass

    def draw(self, screen):
        screen.fill((240, 220, 255))
        draw_text(
            screen,
            f" Ball at {self.ball.position} - PAUSED - Press any key to return",
        )

    def cleanup(self):
        pass


class Ball:
    def __init__(self):
        self.pos = [random() * 800, random() * 800]

    @property
    def position(self):
        return [int(self.pos[0]), int(self.pos[1])]

    def rand_position(self):
        self.pos = [random() * 800, random() * 800]

    def update(self, dt):
        self.pos[0] += dt * 100
        self.pos[1] += dt * 100

    def draw(self, screen):
        pg.draw.circle(screen, (200, 100, 0), self.pos, 10)


def draw_text(screen, text):
    font = pg.font.SysFont(None, 30)
    text_surface = font.render(text, True, (0, 0, 0))
    text_rect = text_surface.get_rect(topleft=(100, 100))
    screen.blit(text_surface, text_rect)
