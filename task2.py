class Clothes:
    value = 0

    def __init__(self, value):
        self.value = value


class Coat(Clothes):
    @property
    def cloth(self):
        return self.value / 6.5 + .5


class Costume(Clothes):
    @property
    def cloth(self):
        return 2*self.value


print(Coat(20).cloth)
