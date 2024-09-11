class Bicycle:
    def _init_(self, brand, model, year, gear_type, wheel_size):
        self.brand = brand
        self.model = model
        self.year = year
        self.gear_type = gear_type
        self.wheel_size = wheel_size
        self.mileage = 0

    def get_description(self):
        return f"{self.year} {self.brand} {self.model} with {self.gear_type} gears and {self.wheel_size} inch wheels."

    def ride(self, miles):
        self.mileage += miles
        return f"You rode {miles} miles. The new mileage is {self.mileage} miles."

    def get_gear_type(self):
        return self.gear_type