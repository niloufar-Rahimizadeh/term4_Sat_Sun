from car import Car
from car import Battery


class ElectricCar(Car):
    def __init__(self, company, model, year):
        super().__init__(company, model, year)
        self.battery = Battery()

    

    def fill_gas_tank(self):
        print("It doesn't need a gas tank")



my_elec = ElectricCar('BMW', 'IX', '2022')


print(my_elec.get_descriptive_name())
my_elec.battery.describe_battery()