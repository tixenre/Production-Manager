import filament

class File:
    def __init__(self, cm3, time):
        # self.idn = idn
        # self.name = name
        # self.file_3mf = file_3mf
        # self.file_stl = file_stl
        self.cm3 = cm3
        self.time = time #in minutes
        # self.cost = cost
        # self.price = price
        # self.update_time = update_time
        

    def cost(self):
        gr = self.cm3* 1.25
        cost= (gr * 1) + (self.time * 0.25)
        return cost

    def price(self):
        cost = File.cost(self)
        price = cost*1.5
        print(price)

a1= File(25,50)

print(a1.cost())
print(a1.price())
