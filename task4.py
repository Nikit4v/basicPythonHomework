# print(max(*list(map(lambda x: int(x), list(input())))))
string = input()
array = list(string)
pointer = 0
cache = 0

while pointer < len(array):
    if cache < int(array[pointer]):
        cache = int(array[pointer])
    pointer += 1

print(cache)