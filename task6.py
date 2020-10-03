_list = [
    {
        "name": input(),
        "price": input(),
        "count": input(),
        "units": input()
    } for m in range(int(input()))
]
print(
    {
        "name": list(set([item["name"] for item in _list])),
        "price": list(set([item["price"] for item in _list])),
        "count": list(set([item["count"] for item in _list])),
        "units": list(set([item["units"] for item in _list]))
    }
)
