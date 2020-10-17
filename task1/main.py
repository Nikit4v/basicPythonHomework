import threading as mp
from classes.data import Data
from functions import main
from os import environ

environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

import sys
print(sys.version_info)

color = Data('r')
proc = mp.Thread(target=main, args=(color,))
proc.start()
while True:
    print("Welcome to Traffic Color!")
    print("Please, choose the renderer:\n"
          "Type 'console' to render in your terminal\n"
          "Type 'graphics' to use the 2D-graphics in new window\n"
          "Type 'OpenGL' to try to use the OpenGL library")
    answer = input(">")
    if answer in ["console", "graphics", "OpenGL"]:
        break
if answer == 'console':
    try:
        import renderers.TermColor

        renderers.TermColor.start(color)
    finally:
        color.set_data("EOF")
elif answer == 'graphics':
    try:
        import renderers.PyGame
        renderers.PyGame.start(color)
    finally:
        color.set_data("EOF")
        proc.join()
elif answer == "OpenGL":
    try:
        import renderers.OpenGL
        renderers.OpenGL.start(color)
    finally:
        color.set_data("EOF")
        proc.join()