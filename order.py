
from customer import Customer
from coffee import Coffee

class Order:

    all = []

    def __init__(self, customer, coffee, price):
       
       if not isinstance(customer, Customer):
           raise TypeError("Customer must be an instance of customer.")
       if not isinstance(coffee, Coffee):
           raise TypeError("Coffee must be an instance of coffee.")
       
       self.__dict__["_locked"] = False

       self.customer = customer
       self.coffee = coffee
       self.price = price

       self.__dict__["_locked"] = True

       Order.all.append(self)

    @property
    def customer(self):
        return self._customer
    
    @customer.setter
    def customer(self, customer):
        if self.__dict__.get("_locked", False):
            raise AttributeError("Order instances are immutable")
        else:
            self._customer = customer
    
    @property
    def coffee(self):
        return self._coffee
    
    @coffee.setter
    def coffee(self, coffee):
        if self.__dict__.get("_locked", False):
            raise AttributeError("Order instances are immutable")
        else:
            self._coffee = coffee
    
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, price):
        if self.__dict__.get("_locked", False):
            raise AttributeError("Order price cannot be modified after being created.")
        if (isinstance(price, (int, float)) and 1.0 <= price <= 10.0):
            self._price = price
        else:
            raise ValueError("Price must be a number between 1.0 and 10.0")
    
