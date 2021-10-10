class Car:
    def __init__(self, company, model, year):
        self.company = company
        self.model = model
        self.year = year
        self.odometer_reading = 400

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.company} {self.model}"
        return long_name.title() 

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage1):
        if mileage1>self.odometer_reading:
            self.odometer_reading = mileage1

    def increment_odometer(self, mileage2):
        if mileage2>0:
            self.odometer_reading += mileage2
            
    def fill_gas_tank(self):
        print("It takes 2 minutes to fill gas tank")
# my_new_car = Car('audi', 'a4', 2019)

# # my_new_car.odometer_reading=15
# # my_new_car.model='Q3'
# # my_new_car.year=2020
# # my_new_car.update_odometer(0)
# # print(my_new_car.get_descriptive_name())
# my_new_car.increment_odometer(-400)
# my_new_car.read_odometer()

class Battery:
    def __init__(self, battery_size=75):
        self.battery_size = battery_size
    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")    
