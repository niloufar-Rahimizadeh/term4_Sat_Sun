class Car:
    def __init__(self, company, model, year):
        self.company = company
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.company} {self.model}"
        return long_name.title() 

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        self.odometer_reading = mileage

my_new_car = Car('audi', 'a4', 2019)



# my_new_car.odometer_reading=15
# my_new_car.model='Q3'
# my_new_car.year=2020
my_new_car.update_odometer(12)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

