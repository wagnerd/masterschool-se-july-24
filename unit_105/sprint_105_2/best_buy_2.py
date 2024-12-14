product_list = [
    "Product1",
    "Product2"
]

for product in product_list:
    print(product)

i = 0
for product in product_list:
    print(f"Index: {i}, {product}")
    i += 1

for index, product in enumerate(product_list, start=1):
    print(f"Index2: {index}, {product}")

class Human():
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

class Female(Human):
    def __init__(self, name, age, has_child=False):
        super().__init__(name, age, gender="f")
        self.gave_birth = has_child

    def give_birth(self):
        self.gave_birth = True

daniel = Human("Daniel", 38, "m")
petra = Female("Petra", 21, True)
petra.give_birth()