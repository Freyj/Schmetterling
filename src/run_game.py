import sys

# The major, minor version numbers you require
MIN_VER = (3, 8)
if sys.version_info[:2] < MIN_VER:
    sys.exit("This game requires Python{}.{}.".format(*MIN_VER))
