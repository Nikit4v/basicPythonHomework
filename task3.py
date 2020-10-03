print("Решение через list")
i = int(input())
winter = [12, 1, 2]
spring = [3, 4, 5]
summer = [6, 7, 8]
autumn = [9, 10, 11]
if i in winter:
    print("It's winter")
elif i in spring:
    print("It's spring")
elif i in summer:
    print("It's summer")
elif i in autumn:
    print("It's autumn")
else:
    print("Incorrect number")
print("Решение через dict")
dict = {
    "1": "winter",
    "2": "winter",
    "3": "spring",
    "4": "spring",
    "5": "spring",
    "6": "summer",
    "7": "summer",
    "8": "summer",
    "9": "autumn",
    "10": "autumn",
    "11": "autumn",
    "12": "winter"
}
while True: print(f"It's {dict.get(input(), 'incorrect number')}")
