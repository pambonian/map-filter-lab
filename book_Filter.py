books = [
    {
        "name": "Marcel Proust",
        "title": "In Search of Lost Time",
        "genre":"Autobiography",
    },
    {
        "name": "James Joyce",
        "title":" Ulysses",
        "genre":"novel",
    },
    {
        "name": "Miguel de Cervantes",
        "title": " Don Quixote",
        "genre": "satire",
    }
]

my_book_list = list(map(lambda x:x,books))

fav_books = list(filter(lambda book: "satire" == book["genre"],books))

print(my_book_list)
print(fav_books)