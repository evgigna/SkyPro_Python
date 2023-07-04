from address import Address

class Mailing:
    to_address = Address('112358', 'Moscow', 'Gagarina', '15', '94')
    from_address = Address('365841', 'Tomsk', 'Lenina', '4', '10')

    def __init__(self, to_address, from_address, cost, track):
        self.to_address = to_address
        self.from_address = from_address
        self.cost = cost
        self.track = track
    
    def printCost(self):
        print('Стоимость', self.cost , 'рублей')