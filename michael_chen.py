products = [
    {
        "name": "Water gun",
        "cost": 10.50
    },
    {
        "name": "Laptop",
        "cost": 459.99
    },
    {
        "name": "Stuffed Animal",
        "cost": 4.99
    },
    {
        "name": "Colored Pencils",
        "cost": 8.99
    },
    {
        "name": "iPad",
        "cost": 489.99
    },
    {
        "name": "socks",
        "cost": 12.49
    },
    {
        "name": "Phone Case",
        "cost": 49.99
    }
]

inflation = list(map(lambda x: x.get("cost") * 1.07, products))
print('Inflation', inflation)

under_50_dollars = list(filter(lambda x: x.get("cost") < 50, products))
print('Products under 50$', under_50_dollars)
