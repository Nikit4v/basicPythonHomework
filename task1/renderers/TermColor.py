from time import sleep
from termcolor import colored
from functions import cls

colors = {"r": ["    ", "####", "####"], "y": ["####", "    ", "####"], "g": ["####", "####", "    "]}


# noinspection PyGlobalUndefined
def start(color):
    while True:
        sleep(1)
        cls()
        print(colored(colors[color.s][0], color="grey", on_color="on_red"))
        print(colored(colors[color.s][0], color="grey", on_color="on_red"))
        print(colored(colors[color.s][1], color="grey", on_color="on_yellow"))
        print(colored(colors[color.s][1], color="grey", on_color="on_yellow"))
        print(colored(colors[color.s][2], color="grey", on_color="on_green"))
        print(colored(colors[color.s][2], color="grey", on_color="on_green"))