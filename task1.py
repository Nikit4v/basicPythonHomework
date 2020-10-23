class Matrix:
    __data = []
    __schema = []

    def __init__(self, x, y, default=0):
        self.__schema = [x, y]
        self.__data = [[default for i in range(y)] for i in range(x)]
        self.default = default
        self.rec = [self]

    def scale(self, x, y):
        if y >= self.__schema[1]:
            for i in self.__data:
                i += [self.default for i in range(y-self.__schema[1])]
        elif y < self.__schema[1]:
            for j, i in enumerate(self.__data):
                self.__data[j] = i[:y]
        if x >= self.__schema[0]:
            self.__data += [[self.default for i in range(y)] for i in range(x - self.__schema[0])]
        else:
            self.__data = self.__data[:x]
        self.__schema = [x, y]

    def __add__(self, other):
        maxes = [max(self.__schema[0], other.__schema[0]), max(self.__schema[1], other.__schema[1])]
        self.scale(*maxes)
        other.scale(*maxes)
        out = Matrix(*maxes)
        for i in range(len(self.__data)):
            for j in range(len(self.__data[i])):
                out.__data[i][j] = \
                    self.__data[i][j] + other.__data[i][j]
        return out

    def __str__(self):
        pr = [' '.join((map(lambda a: str(a), i))) for i in self.__data]
        # print(self.rec)
        return '\n'.join(pr)


m = Matrix(4, 4, 100)
print(m)
print()
m = m + Matrix(10, 10, 5)
print(m)
print()
m.scale(5, 5)
print(m)
print()
m.scale(3, 3)
print(m)
print()
m.scale(2, 10)
print(m)
