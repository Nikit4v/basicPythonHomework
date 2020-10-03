# Заполнение данными
import random

# noinspection LongLine
data = [random.choice((random.random(), str(random.random()), [i for i in range(random.randint(0, 100))]))
        for i in range(int(input("Введите размер массива: ")))]

# Код для проверки
for i in data:
    print(type(i))
