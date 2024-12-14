class Dog:

    def __init__(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def set_name(self, new_name):
        if not new_name:
            print("Cannot change name to an empty name!")
        else:
            self._name = new_name

rexi = Dog("Rexi")
rexi.set_name("")
print(rexi.get_name())
