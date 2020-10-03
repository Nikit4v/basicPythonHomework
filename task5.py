import random
_list = [random.randint(1, i+1) for i in range(int(input()))]
_list.sort()

while True:
    try:
        _list.append(int(input()))
    except ValueError:
        print("Something wrong. Please, try again")
    _list.sort(reverse=True)
    print(_list)
