class Road:
    def __init__(self, length,width):
        self._length = length
        self._width = width

    def calculate(self):
        return self._length * self._width * 25 * 5

    @property
    def mass(self):
        return self.calculate()