from time import sleep


# noinspection PyGlobalUndefined
from classes.data import Data


class TrafficColor:
    __color = "r"

    def __init__(self, color: Data):
        self.Data_object = color

    def running(self):
        try:
            while True:
                sleep(7)
                self.__color = "y"
                self.global_update()
                sleep(2)
                self.__color = "g"
                self.global_update()
                sleep(5)
                self.__color = "y"
                self.global_update()
                sleep(2)
                self.__color = "r"
                self.global_update()
        except Exception:
            return

    def global_update(self):
        color = self.Data_object
        if color.s == "EOF":
            raise Exception
        color.set_data(self.__color)
