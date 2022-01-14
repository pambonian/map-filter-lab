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
    },
    {
        "name": "Paper Plates",
        "category": "Paper",
        "price": 7
    }
]

product_list = list(map(lambda x:x,products))

check_price = list(filter(lambda x: x.get("price") < 10, products))

print(product_list)
print(check_price, "check price")