class Mouse:
    def __init__(self):
        self.x = 0
        self.y = 0

        self.left = 0
        self.middle = 0
        self.right = 0

        self.left_held = 0
        self.middle_held = 0
        self.right_held = 0

    def reset_buttons(self):
        self.left = 0
        self.middle = 0
        self.right = 0

    def update_coordinates(self, mouse_pos):
        self.x, self.y = mouse_pos

    def process_button_down(self, mouse_state):
        """Process a pygame.MOUSEBUTTONDOWN event."""
        self.left_held, self.middle_held, self.right_held = mouse_state

    def process_button_up(self, mouse_state):
        """Process a pygame.MOUSEBUTTONUP event."""
        if self.left_held and not mouse_state[0]:
            self.left = 1
            self.left_held = 0
        if self.middle_held and not mouse_state[1]:
            self.middle = 1
            self.middle_held = 0
        if self.right_held and not mouse_state[2]:
            self.right = 1
            self.right_held = 0

    def is_in(self, start_x, start_y, end_x, end_y):
        return start_x < self.x < end_x and start_y < self.y < end_y
