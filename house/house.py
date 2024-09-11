class House:
    def _init_(self, address, num_bedrooms, num_bathrooms, square_footage):
        self.address = address
        self.num_bedrooms = num_bedrooms
        self.num_bathrooms = num_bathrooms
        self.square_footage = square_footage

    def get_details(self):
        return f"House at {self.address} with {self.num_bedrooms} bedrooms, {self.num_bathrooms} bathrooms, and {self.square_footage} square feet."

    def add_bedroom(self):
        self.num_bedrooms += 1
        return f"Added a bedroom. The new total is {self.num_bedrooms} bedrooms."