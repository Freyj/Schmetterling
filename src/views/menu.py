import arcade
from src.constants import SCREEN_WIDTH, SCREEN_HEIGHT
from src.views.game import GameView


class MenuView(arcade.View):

    def __init__(self):
        super().__init__()
        # Create variables here

        self.menu_music = arcade.load_sound("sounds/Harp.ogg")

    def on_show(self):
        arcade.set_background_color(arcade.color.CORNFLOWER_BLUE)
        self.menu_music.play(0.2)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("Schmetterling, a PyWeek experience", SCREEN_WIDTH/2, SCREEN_HEIGHT/2,
                         arcade.color.VIVID_AUBURN, font_size=30, anchor_x="center")
        arcade.draw_text("Click to start", SCREEN_WIDTH/2, SCREEN_HEIGHT/2 - 40,
                         arcade.color.ALIZARIN_CRIMSON, font_size=10, anchor_x="center")
        arcade.draw_text("Harp music by VWolfdog - CC-BY 3.0", 0.5 * SCREEN_WIDTH, 0.1 * SCREEN_HEIGHT,
                         arcade.color.BLACK, font_size=14, anchor_x="center")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        game_view = GameView()
        game_view.setup()
        self.window.show_view(game_view)

