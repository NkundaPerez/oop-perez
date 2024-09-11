class Motorcycle:
    def _init_(self, make, model, year, engine_size, mileage):
        self.make = make
        self.model = model
        self.year = year
        self.engine_size = engine_size
        self.mileage = mileage

    def get_description(self):
        return f"{self.year} {self.make} {self.model} with {self.engine_size}cc engine and {self.mileage} miles."

    def ride(self, miles):
        self.mileage += miles
        return f"You rode {miles} miles. The new mileage is {self.mileage} miles."

    def get_engine_size(self):
        return self.engine_size