class Inventory:
    def __init__(self):
        self.inventory = {}

    def add_item(self, item_name, quantity, price):
        self.inventory[item_name] = {'quantity': quantity, 'price': price}

    def update_item(self, item_name, new_quantity, new_price):
        if item_name in self.inventory:
            self.inventory[item_name]['quantity'] = new_quantity
            self.inventory[item_name]['price'] = new_price

    def remove_item(self, item_name):
        if item_name in self.inventory:
            del self.inventory[item_name]

    def generate_report(self):
        print("Inventory Report:")
        for item_name, item_info in self.inventory.items():
            print(f"{item_name}: Quantity - {item_info['quantity']}, Price - ${item_info['price']}")

# Example usage:
inventory_manager = Inventory()
inventory_manager.add_item("Product A", 50, 10.99)
inventory_manager.add_item("Product B", 30, 5.99)
inventory_manager.update_item("Product A", 40, 12.99)
inventory_manager.remove_item("Product B")
inventory_manager.generate_report()
