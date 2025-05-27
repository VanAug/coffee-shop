
class Customer:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 15:
            self._name = name
        else:
            raise ValueError("Name must be a string")

    #Customer.orders
    def orders(self):
        from order import Order
        return [order for order in Order.all if order.customer == self]
    
    #Customer.coffees
    def coffees(self):
        return list({order.coffee for order in self.orders()})
    
    #Customer.create_order(coffee, price)
    def create_order(self, coffee, price):
        from order import Order
        return Order(self, coffee, price)
    
    #Customer.most_aficionado(coffee)
    @classmethod
    def most_aficionado(cls, coffee):
        #get all coffee orders
        orders = coffee.orders()
        if not orders:
            return None

        #trck total spending per customer
        customer_spending = {}
        for order in orders:
            customer = order.customer

            if customer in customer_spending:
                customer_spending[customer] += order.price
            else:
                customer_spending[customer] = order.price

        #find customer with maximum spending
        max_spending = max(customer_spending.values())
        top_customers = [
            customer for customer, total in customer_spending.items()
            if total == max_spending
        ]

        return top_customers