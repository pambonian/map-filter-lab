from unicodedata import category


products = [
    {
        "name": "Shampoo",
        "category": "Soap",
        "price": 10
    },
    {
        "name": "Kleenex",
        "category": "Paper",
        "price": 8
    }
]

prices = [12, 13, 11, 18, 45, 65, 32]

product_list = list(map(lambda x:x,products))

check_price = list(filter(lambda x: x.get("price") < 10, products))

print(product_list)
print(check_price, "check price")