class Product():

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Product: {self.name}"

    def __repr__(self):
        return f"Product: {self.name}"

class ProductList(list):

    def __init__(self):
        super().__init__()

    def __getitem__(self, item):
        if type(item) == int:
            return self.



prod1 = Product("prod1")
prod2 = Product("prod2")

product_list = ProductList()

product_list.append(prod1)
product_list.append(prod2)

print(product_list)

print(product_list[0])

