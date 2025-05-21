class Person:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        return f"Hi, I’m {self.name}"

p = Person("Akash")
print(p.say_hello())
