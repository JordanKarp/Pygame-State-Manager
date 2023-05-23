class State:
    """Default class for a game state"""

    def __init__(self):
        """Init"""
        self.next_state = None
        self.persist = {}

    def startup(self, persistent=None):
        """Upon state startup"""
        if persistent is None:
            persistent = {}
        self.next_state = self
        self.persist = persistent

    def handle_event(self, event):
        """Handle pygame events"""

    def update(self, dt):
        """Update state"""

    def draw(self, screen):
        """Draw state"""

    def cleanup(self):
        """Upon leaving state"""
