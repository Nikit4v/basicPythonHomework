# Почему комментарии? Названия переменных непонятные.

_in = input()  # Выручка
_out = input()  # Издержки
_count = input()  # Количество сотрудников

_profit = _in - _out  # Вычисление прибыли

if _profit > 0:
    _rent = _profit/_in
    print(_profit, _rent, _profit/_count)
else:
    print(_profit)