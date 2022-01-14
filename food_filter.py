foods = [
    { "name": "banana" , "type":"fruit"},
    { "name": "cheetos" , "type":"chips"},
    { "name": "apple" , "type":"fruit"},
    { "name": "milk" , "type":"dairy"},
    { "name": "lays" , "type":"chips"},
    { "name": "pear" , "type":"fruit"},
]

food_to_buy = list(map(lambda x:x,foods))

fav_foods = list(filter(lambda food: "chips" == food["type"],foods))
print(food_to_buy)
print(fav_foods)
