_list = [input() for i in range(int(input("Количество элементов в масиве:")))]
for i in range(len(_list)):
    if i % 2 == 0:
        continue
    _list[i], _list[i-1] = _list[i-1], _list[i]
print(_list)
