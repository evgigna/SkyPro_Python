class Smartphone:
    def __init__(self, phone_brand, phone_model, phone_number):
        self.phone_brand = phone_brand
        self.phone_model = phone_model
        self.phone_number = phone_number
    
    def __str__(self):
        return "{} {} {}".format(self.phone_brand, self.phone_model, self.phone_number)