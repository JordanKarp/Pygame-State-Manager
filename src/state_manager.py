import sys
import pygame as pg


class StateManager:
    def __init__(self, screen, states, starting_state, fps=60):
        """
        __init__ _summary_

        Args:
            screen (_type_): _description_
            clock (_type_): _description_
            states (dict): A dictionary of the state name to state class.
            starting (str): Starting state, the key in the states dictionary.
            fps (int, optional): Frames per second. Defaults to 60.
        """
        self.fps = fps
        self.screen = screen
        self.states = states
        self.state_name = starting_state
        self.clock = pg.time.Clock()

        self.current_state = self.states[self.state_name]
        self.flip_state(self.state_name)
        self.previous_state_name = None

    def get_fps(self):
        """Returns the current FPS"""
        return self.clock.get_fps()

    def flip_state(self, specified_state=None):
        """Handles changing states properly.

        Args:
            specified_state(str): Defines the state to flip to. If None, flips to previous state.
        """
        if not specified_state:
            specified_state = self.previous_state_name
        self.current_state.cleanup()
        persistent = self.current_state.persist
        self.previous_state_name = self.state_name
        self.state_name = specified_state
        self.current_state = self.states[self.state_name]
        self.current_state.startup(persistent)

    def event_loop(self):
        """Event loop"""
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            else:
                self.current_state.handle_event(event)

    def update(self, dt):
        """Update the current state"""
        self.current_state.update(dt)

    def draw(self):
        """Draw the current state"""
        self.current_state.draw(self.screen)
        pg.display.flip()

    def run(self):
        """Main Program Loop"""
        while True:
            if self.current_state != self.current_state.next_state:
                self.flip_state(self.current_state.next_state)

            dt = self.clock.tick(self.fps) / 1000
            self.event_loop()
            self.update(dt)
            self.draw()
