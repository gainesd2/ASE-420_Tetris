class Level:
    def __init__(self):
        self.level = 1

    def update_level(self, score):
        if score > 3:
            self.level = 2
        if score > 6:
            self.level = 3
        if score > 9:
            self.level = 4

    def get_level(self):
        return self.level

    def write_level(self, screen, text):
        text = f"Level: {text.get_clock_level()}"
        screen.add_text(
            font_type='Calibri',
            font_size=25,
            text=text,
            render_bool=True,
            color=(255, 125, 0),
            appearance_range=[0, 60])
