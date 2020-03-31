import filament
from itertools import count


class Presupuesto:

    mode = {'servicio': 2, 'producto': 1.5, 'mardel3d': 1.1}
    comision = {'cash': 1, 'mercadopago': 1.06,
                'mercadolibre_clasic': 1.13, 'mercadolibre_gold': 1.23}
        
    @property
    def get_cost(self,kind='PLA',cm3=None,time=None):
        if gr == None:
            gr = filament.cm3_to_gr(kind, cm3)
        else:
            pass
        gr_cost = filament.kind_gr_cost(kind)
        cost =  (gr*gr_cost) + time
        return cost


    # def get_price(self, mode):
    #     p = self.cost*mode
    #     price = {key: int(value*p) for (key, value) in self.comision.items()}
    #     return price

p1 = Presupuesto(kind='PLA', cm3=1000, time=0)
# p2 = Presupuesto('PETG', cm3=1000, time=0)
# p1 = Presupuesto('PLA', cm3=1000, time=0)

if __name__ == "__main__":
    print(p1.get_cost)
    # print(p2.cost)
    # print(p1.servicio)
    # print(p2.servicio)
    # print(p1.producto)
    # print(p2.producto)
    # print(p1.mardel3d)
    # print(p2.mardel3d)
