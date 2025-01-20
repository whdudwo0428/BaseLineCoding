class Book():
    def __init__(self,title, author,price):
        self.title = title
        self.author = author
        self.price = price

    def display_info(self):
        print("Book's title : ", self.title)
        print("Book's author : ", self.author)
        print("Book's price : ", self.price)

    def __eq__(self, other):
        if self.price == other.price:
            print("Ture")
        else:
            print("None")

book1 = Book("aaa", "AAA", 5000)
book2 = Book("bbb","BBB", 6000)
book1.__eq__(book2)
book1.display_info()
"""
lt는 less than, <
le는 less or equal, <= 
eq는 equal, ==
ne는 not equal !=
gt는 great than, >
ge는 gret or equal >=

"""