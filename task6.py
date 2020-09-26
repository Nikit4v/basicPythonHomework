a = 2
b = 3
index = 0
num = a
while True:
    index += 1
    num += num * 0.1
    print(num)
    if num > b:
        break

print(index+1)