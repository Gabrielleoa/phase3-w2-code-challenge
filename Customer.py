class Customer:
    def __init__(self, given_name, last_name):
        self.given_name= given_name
        self.last_name = last_name
    def given_name(self):
        return self.given_name
    def last_name(self):
        return self.last_name
    def full_name(self):
        return (f'{self.given_name}') +  (f'{self.last_name}')
    def all_names(self):
        return self.Customer  

customer_one = Customer('George', 'Washington')
print(customer_one.full_name())

