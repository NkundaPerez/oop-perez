class Shoe:
    def _init_(self, name, product_code, quantity, value_per_item):
        self.name = name
        self.product _code = product_code
        self.quantity = quantity
        self.value_per_item = value_per_item

    def get_description(self):
        return f"{self.name} with product code {self.product_code}."

    def get_total_value(self):
        return self.quantity * self.value_per_item

    def get_quantity(self):
        return self.quantity

    def set_quantity(self, new_quantity):
        self.quantity = new_quantity
        return f"Quantity updated to {self.quantity}."

    def get_value_per_item(self):
        return self.value_per_item

    def set_value_per_item(self, new_value_per_item):
        self.value_per_item = new_value_per_item
        return f"Value per item updated to {self.value_per_item}."