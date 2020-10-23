class Cell:
    def __init__(self, count: int):
        self.count = count

    def __add__(self, other):
        return Cell(self.count + other.count)

    def __sub__(self, other):
        if self.count == other.count:
            print("Одинаковое количесво клеток")
            return
        return Cell(self.count - other.count)

    def __mul__(self, other):
        return Cell(self.count * other.count)

    def __truediv__(self, other):
        if self.count % other.count / other.count <= 0.5:
            Cell(self.count // other.count)
        else:
            Cell(other.count // self.count + 1)

    def __str__(self):
        return str(self.count)

    def make_order_helper(self, count):
        l = ("* " * self.count)[:-1].split(" ")
        for i in range(0, self.count, count):
            yield ''.join(l[i:i + count])

    def make_order(self, count):
        l = list(self.make_order_helper(count))
        return '\n'.join(l)


print(Cell(10).make_order(5))
print(Cell(20) + Cell(30))
