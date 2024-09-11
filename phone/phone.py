class Phone:
    def _init_(self, brand, model, year, storage_capacity, battery_life):
        self.brand = brand
        self.model = model
        self.year = year
        self.storage_capacity = storage_capacity
        self.battery_life = battery_life
        self.contacts = {}

    def get_description(self):
        return f"{self.year} {self.brand} {self.model} with {self.storage_capacity}GB storage and {self.battery_life} hours battery life."

    def add_contact(self, name, number):
        self.contacts[name] = number
        return f"Contact {name} with number {number} added."

    def get_contact(self, name):
        if name in self.contacts:
            return f"Contact {name} has number {self.contacts[name]}."
        else:
            return f"No contact found with name {name}."

    def get_storage_capacity(self):
        return self.storage_capacity