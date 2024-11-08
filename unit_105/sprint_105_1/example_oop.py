class MyClass1:
    def __init__(self):
        self.var1 = "test"

    def run(self):
        self.var1 = "run"
        print("")

class MyClass2:
    def __init__(self, var1, var2):
        self.var1 = var1
        self.var2 = var2

    @property
    def same(self):
        return self.var1 == self.var2
