import filament

class Presupuesto:

    mode = {'servicio': 2, 'producto': 1.5, 'mardel3d': 1.1}
    comision = {'cash': 1, 'mercadopago': 1.06, 'mercadolibre_clasic': 1.13, 'mercadolibre_gold':1.23}

    def __init__(self, kind, cm3, time):
        self.kind = kind
        self.cm3 = cm3
        self.time = time
        self.gr = filament.cm3_to_gr(self.kind,self.cm3)
        self.cost = self.get_cost()
        self.servicio = self.get_price(self.mode['servicio'])
        self.producto = self.get_price(self.mode['producto'])
        self.mardel3d = self.get_price(self.mode['mardel3d'])
        

    def get_cost(self):
        if self.gr == None:
            self.gr = filament.cm3_to_gr(self.kind, self.cm3)
        else:
            pass
        gr_cost = filament.kind_gr_cost(self.kind)
        cost = (self.gr*gr_cost) + self.time
        return cost

    def get_price(self,mode):
        p= self.cost*mode
        price = {key:int(value*p) for (key,value) in self.comision.items()}
        return price


p1=Presupuesto('PLA',1000,0)
p2=Presupuesto('PETG',1000,0)

print(p1.cost)
print(p2.cost)
print(p1.servicio)
print(p2.servicio)
print(p1.producto)
print(p2.producto)
print(p1.mardel3d)
print(p2.mardel3d)