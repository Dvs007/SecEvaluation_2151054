import tkinter as tk

class StoreGUI:
    def __init__(self, root):
        self.root = root
        self.cart = []
        self.products = {
            "Product A": 10.99,
            "Product B": 5.99,
            "Product C": 7.99
        }
        self.create_gui()

    def create_gui(self):
        # GUI components go here
        self.root.title("Store GUI")
        
        # Product list
        self.product_listbox = tk.Listbox(self.root)
        for product in self.products:
            self.product_listbox.insert(tk.END, f"{product} - ${self.products[product]}")
        self.product_listbox.pack()

        # Cart
        self.cart_label = tk.Label(self.root, text="Shopping Cart")
        self.cart_label.pack()
        self.cart_listbox = tk.Listbox(self.root)
        self.cart_listbox.pack()

        # Add to Cart button
        self.add_to_cart_button = tk.Button(self.root, text="Add to Cart", command=self.add_to_cart)
        self.add_to_cart_button.pack()

        # Total Cost
        self.total_cost_label = tk.Label(self.root, text="Total Cost: $0.00")
        self.total_cost_label.pack()

    def add_to_cart(self):
        selected_product = self.product_listbox.get(tk.ACTIVE)
        product_name = selected_product.split(" - ")[0]
        self.cart.append(product_name)
        self.update_cart_listbox()
        self.update_total_cost()

    def update_cart_listbox(self):
        self.cart_listbox.delete(0, tk.END)
        for item in self.cart:
            self.cart_listbox.insert(tk.END, item)

    def update_total_cost(self):
        total_cost = sum([self.products[item] for item in self.cart])
        self.total_cost_label.config(text=f"Total Cost: ${total_cost:.2f}")

if __name__ == "__main":
    root = tk.Tk()
    app = StoreGUI(root)
    root.mainloop()
