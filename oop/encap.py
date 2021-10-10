class Fish:

    def __init__(self):
        self.__size = "big"

    def get_size(self):
        print("I'm a " + self.__size + " fish")

    def set_size(self, new_size):
        self.__size = new_size 


my_fish = Fish()

my_fish.__size = "small"
# my_fish.set_size("small")
my_fish.get_size()