import sys

import arcade

from src.constants import SCREEN_WIDTH, SCREEN_HEIGHT


class EndView(arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("Game Over - press SPACE to quit", SCREEN_WIDTH/2, SCREEN_HEIGHT/2,
                         arcade.color.WHITE, 30, anchor_x="center")

    def on_key_press(self, key, _modifiers):
        if key == arcade.key.SPACE:
            sys.exit()
