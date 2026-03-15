#7. Book Shop Inventory System

class Book:
    def __init__(self, author, title, price, publisher, stock):
        self.author = author
        self.title = title
        self.price = price
        self.publisher = publisher
        self.stock = stock

books = [
    Book("James", "Python", 500, "TechPress", 10),
    Book("John", "Java", 450, "CodePub", 5),
    Book("Alice", "C++", 400, "LearnPub", 8)
]

title = input("Enter book title: ")
author = input("Enter author name: ")

found = False

for b in books:
    if b.title == title and b.author == author:
        found = True

        print("Book Available")
        print("Title:", b.title)
        print("Author:", b.author)
        print("Price:", b.price)
        print("Publisher:", b.publisher)
        print("Stock:", b.stock)

        copies = int(input("Enter number of copies required: "))

        if copies <= b.stock:
            cost = copies * b.price
            print("Total Cost:", cost)
        else:
            print("Required number of copies are not available")

if not found:
    print("Book not available")