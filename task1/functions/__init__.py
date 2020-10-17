import os
from classes.trafficcolor import TrafficColor


def cls():
    os.system("cls" if os.name == "nt" else "clear")


def main(color):
    tc = TrafficColor(color)
    tc.running()