class Review:
    def __init__(self, customer, restuarant, rating):
        self.customer = customer
        self.restaurant = restuarant
        self.rating = rating
    def rating(self):
        return self.rating
    def all_reviews(self):
        return (f'{self.restaurant}' + f'{self.customer}' + f'{self.rating}')

first_rating= Review('Gabrielle', 'La Bodega', 10)
print(first_rating.rating)