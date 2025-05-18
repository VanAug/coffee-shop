
class Coffee:
    def __init__(self, name):
        
        self.__dict__["_locked"] = False
        self.name = name
        self.__dict__["_locked"] = True

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if self.__dict__.get("_locked", False):
            raise AttributeError("Coffee name cannot be modified after being created")
        if isinstance(name, str) and len(name) >= 3:
            self._name = name
        else:
            return ValueError("Name must be a string")
        
    def __setattr__(self, key, value):
        if self.__dict__.get("_locked", False):
            raise AttributeError("Coffee instances are immutable")
        super().__setattr__(key, value)

    #Coffee.orders
    def orders(self):
        from order import Order
        return [order for order in Order.all if order.coffee == self]
    
    #Coffee.customers
    def customers(self):
        return list({order.customer for order in self.orders})