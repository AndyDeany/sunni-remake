import pygame


class Key:

    all = {}

    """Class for representing a key on the keyboard."""
    def __init__(self, keycode):
        self.keycode = keycode
        self.just_pressed = False
        self.is_pressed = False
        self.all[self.keycode] = self

    def __bool__(self):
        return self.just_pressed

    def down(self):
        self.just_pressed = True
        self.is_pressed = True

    def up(self):   # pylint: disable=invalid-name
        self.is_pressed = False


class Keys:
    def __init__(self, game):
        self.game = game

        pygame.key.set_repeat(500, 50)

        self.keys_pressed = 0
        self.receiving_text_input = False
        self.text_input = ""
        self.maximum_characters = 0

        self.backspace = Key(8)
        self.enter = Key(13)
        self.escape = Key(27)
        self.numpad_enter = Key(1073741912)

    def __getitem__(self, keycode):
        try:
            return Key.all[keycode]
        except KeyError:
            print(f"Generating Key({keycode}) instance.")
            return Key(keycode)

    @staticmethod
    def reset():
        for key in Key.all.values():
            key.just_pressed = False

    def start_text_input(self, maximum_characters, *, default_text=""):
        self.receiving_text_input = True
        self.text_input = default_text
        self.maximum_characters = maximum_characters
        pygame.key.start_text_input()

    def process_text_input(self, text_input_event):
        new_text = self.text_input + text_input_event.text
        if len(new_text) <= self.maximum_characters:
            self.text_input = new_text

    def process_text_input_special_keys(self):
        """Process special keys like backspace in the context of text input."""
        if not self.receiving_text_input:
            return
        if self.backspace and self.text_input:
            self.text_input = self.text_input[:-1]
        # Could have code for arrow keys with a cursor and the delete key here. Not a big priority though.

    def stop_text_input(self):
        pygame.key.stop_text_input()
        self.receiving_text_input = False
        return self.text_input

    def process_key_down(self, key_down_event):
        self[key_down_event.key].down()

    def process_key_up(self, key_up_event):
        self[key_up_event.key].up()
