import arcade
from src.constants import SCREEN_WIDTH, SCREEN_HEIGHT
from src.views.end import EndView


class GameView(arcade.View):

    def __init__(self):
        super().__init__()
        # Create variables here

    def setup(self):
        # Replace 'pass' with the code to set up your game
        pass

    def on_show(self):
        arcade.set_background_color(arcade.color.ORANGE_PEEL)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("Game - press SPACE to advance", SCREEN_WIDTH/2, SCREEN_HEIGHT/2,
                         arcade.color.BLACK, font_size=30, anchor_x="center")

    def on_key_press(self, key, _modifiers):
        if key == arcade.key.SPACE:
            end_view = EndView()
            self.window.show_view(end_view)
