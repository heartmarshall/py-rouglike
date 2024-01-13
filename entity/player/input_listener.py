import keyboard

class InputListener:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(InputListener, cls).__new__(cls)
            cls._instance._initiated = False
        return cls._instance

    def __init__(self, world):
        if not self._initiated:
            self._button_actions = {}
            self.world = world

    def add_button(self, key, action):
        self._button_actions[key] = action
    
    def remove_button(self, key):
        if key in self._button_actions:
            del self._button_actions[key]

    def listen_input(self):
        pressed_key_event = keyboard.read_event(suppress=True)
        if pressed_key_event.event_type == keyboard.KEY_DOWN:
            pressed_key = pressed_key_event.name
            if pressed_key in self._button_actions:
                action = self._button_actions[pressed_key]
                action()
            else:
                pass
    
    