import sys
import pygame as pg

from state_manager import StateManager
from demo_states import Game, Pause

WIDTH, HEIGHT = 800, 800
GAME_NAME = "State Manager Demo"
FPS = 60


def run():
    pg.init()
    pg.display.set_caption(GAME_NAME)
    screen = pg.display.set_mode((WIDTH, HEIGHT))

    game_states = {
        "GAME": Game(),
        "PAUSE": Pause(),
    }

    game_manager = StateManager(screen, game_states, "GAME", FPS)

    game_manager.run()
    pg.quit()
    sys.exit()


if __name__ == "__main__":
    run()
