class Address:
    def __init__(self, index, city, street, house, apartment):
        self.index = index
        self.city = city
        self.street = street
        self.house = house
        self.apartment = apartment

class Mailing:
    def __init__(self, to, frm, cost, track):
        self.to = to
        self.from_ = frm
        self.cost = cost
        self.track = track