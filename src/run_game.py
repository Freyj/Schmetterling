import sys
import arcade
from src.constants import MIN_VER, SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE

# The major, minor version numbers you require
from src.views.menu import MenuView

if sys.version_info[:2] < MIN_VER:
    sys.exit("This game requires Python{}.{}.".format(*MIN_VER))


if __name__ == "__main__":
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    menu_view = MenuView()
    window.show_view(menu_view)
    arcade.run()
