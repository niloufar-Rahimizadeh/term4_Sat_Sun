class Dog:
    type = 'Husky'
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(f"{self.name} is sitting now.")

    def roll_over(self):
        print(f"{self.name} rolled over.")


my_dog = Dog('wielli', '5')
your_dog = Dog('Jack', '4')

# print(my_dog.age)
# print(my_dog.name)
# print(20*"*")
# print(your_dog.age)
# print(your_dog.name)


# print(Dog.type)

my_dog.sit()
your_dog.roll_over()