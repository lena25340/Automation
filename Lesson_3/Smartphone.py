class Smartphone:

    def __init__(self, phone_brand, phone_model, subscriber_number):
        self.phone_brand = phone_brand
        self.phone_model = phone_model
        self.subscriber_number = subscriber_number

    def brand(self):
        print(self.phone_brand)

    def model(self):
        print(self.phone_model)

    def number(self):
        print(self.subscriber_number)

    def brandmodelnumber(self):
        print(self.phone_brand, self.phone_model, self.subscriber_number)
