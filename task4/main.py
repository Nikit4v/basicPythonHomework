class Car:
    direction = None
    speed = 100
    current_speed = 0
    color = "red"
    name = "CYBERTRUCK"
    is_police = False

    def __init__(self, speed=100, color="red", name="CYBERTRUCK", is_police=False):
        self.speed: int = speed
        self.color: str = color
        self.name: str = name
        self.is_police: bool = is_police

    log = []

    def go(self):
        self.current_speed = self.speed
        self.log.append(f"Updating speed [speed = {self.current_speed}]")

    def stop(self):
        self.current_speed = 0
        self.log.append(f"Updating speed [speed = {self.current_speed}]")

    def turn(self, direction):
        self.direction = direction
        self.log.append(f"Updating direction [direction = {direction}]")

    def show_speed(self):
        return self.current_speed


class TownCar(Car):
    def show_speed(self):
        if self.current_speed > 60:
            print("Слишком высокая скорость")
        return self.current_speed


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.current_speed > 40:
            print("Слишком высокая скорость")
        return self.current_speed


class PoliceCar(Car):
    def __init__(self, speed=100, color="red", name="CYBERTRUCK", is_police=True):
        super().__init__(speed, color, name, is_police)