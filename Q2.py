class SalesDatabase:
    def __init__(self):
        self.sales_data = []

    def record_sale(self, customer_name, items_purchased, total_amount):
        self.sales_data.append({'customer_name': customer_name, 'items_purchased': items_purchased, 'total_amount': total_amount})

    def calculate_total_sales(self, period_start, period_end):
        total_sales = 0
        for sale in self.sales_data:
            if period_start <= sale['date'] <= period_end:
                total_sales += sale['total_amount']
        return total_sales

    def generate_sales_report(self):
        print("Sales Report:")
        for sale in self.sales_data:
            print(f"Customer: {sale['customer_name']}, Items Purchased: {', '.join(sale['items_purchased'])}, Total Amount: ${sale['total_amount']}")

# Example usage:
sales_db = SalesDatabase()
sales_db.record_sale("Customer A", ["Product A", "Product B"], 25.99)
sales_db.record_sale("Customer B", ["Product A", "Product C"], 35.99)
total_sales = sales_db.calculate_total_sales("2023-01-01", "2023-01-31")
sales_db.generate_sales_report()
