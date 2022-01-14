items = [ 
    {'name': "Shampoo", 'price': 12},
    {'name': "Soap", 'price' : 5},
    {'name': "Deodorant", 'price': 8},
    {'name': "Toothpaste", 'price': 12}
]


def add_up(items):
    receipt_obj = {}

    for item in items:
        name = item.get('name')
        price = item.get('price')
        print(name)

        if (receipt_obj.get(name)):
            receipt_obj[name] += price

        else:
            receipt_obj[name] = price

    return receipt_obj

print(add_up(items))
