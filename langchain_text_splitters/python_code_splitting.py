from langchain.text_splitter import RecursiveCharacterTextSplitter, Language


code = """
class Animal:
    def __init__(self, name, species):
        self.name = name        # public attribute
        self._species = species # protected attribute
        self.__health = 100     # private attribute

    def make_sound(self):
        return "Some generic sound"

    def get_health(self):
        return self.__health

    def take_damage(self, amount):
        self.__health -= amount
        if self.__health < 0:
            self.__health = 0
        return self.__health

    def __str__(self):
        return f"{self.name} the {self._species}"

# Inheritance: Dog is a subclass of Animal
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, species="Dog")
        self.breed = breed

    def make_sound(self):
        return "Woof! Woof!"

# Inheritance: Cat is a subclass of Animal
class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name, species="Cat")
        self.color = color

    def make_sound(self):
        return "Meow!"

# Using the classes
dog1 = Dog("Buddy", "Golden Retriever")
cat1 = Cat("Whiskers", "White")
"""


splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON,
    chunk_size = 400,
    chunk_overlap = 0
)

chunks = splitter.split_text(text=code)

print(len(chunks))
print(chunks[0])