menu = [ 
    {'name': "foie gras", 'price': 120},
    {'name': "caesar salad", 'price' : 5},
    {'name': "marzipan", 'price': 18},
    {'name': "steak", 'price': 75}
]

food_list = list(map(lambda x:x,menu))
print("menu items", food_list)

taxes_per_item = list(map(lambda x: x.get("price") * .15, menu))
print('Total', taxes_per_item)

