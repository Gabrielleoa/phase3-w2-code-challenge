class Review:
    def __init__(self, customer, restuarant, rating):
        self._customer = customer
        self._restaurant = restuarant
        self.rating = rating
    def rating(self):
        return self.rating
    def all_reviews(self):
        return (f'{self.restaurant}' + f'{self.customer}' + f'{self.rating}')
    def customer(self):
        return self._customer
    def restaurant(self):
        return self._restaurant

first_rating= Review('Gabrielle', 'La Bodega', 10)
print(first_rating.rating)

