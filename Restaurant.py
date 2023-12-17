class Restaurant:
    def __init__(self, name):
        self._name= name
    def restaurant_name(self):
        return self._name
    def customer(self, customer):
        self.customer= customer
        return self.customer
    def reviews(self):
        return self._name
    
restaurant= Restaurant(name='La Bodega')
print(restaurant._name)

