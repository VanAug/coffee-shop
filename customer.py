
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
            return ValueError("Name must be a string")

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