class Restaurant:
    def __init__(self, name):
        self._name= name
    def restaurant_name(self):
        return self._name
restaurant= Restaurant(name='La Bodega')
print(restaurant._name)
