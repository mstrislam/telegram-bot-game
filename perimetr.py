class Perimetr:
    def __init__(self,dlinna_pm,storona_pm):
        self.dlinna=dlinna_pm
        self.storona=storona_pm

    def calculate_Perimetr(self):
        result = ( self.dlinna+self.storona)*2
        return result
r1 = Perimetr1(dlinna_pm=4,storona_pm=5)

Perimetr1=r1.calculate_square

print(Perimetr1)