class Filament:

    
    kind_density = {'PLA':1.25, 'PETG':1.27, 'FLEX':1.25, 'ABS':1.27} #density['PLA']

    def __init__(self, kind, vendor, spool_cost, spool_gr=1000):
        self.kind = "kind"
        self.vendor = "vendor"
        self.spool_cost = float(spool_cost)
        self.spool_gr = int(spool_gr)
        self.gr_cost = float(self.spool_cost/self.spool_gr)
        self.density = self.kind_density[kind]

def kind_gr_cost(kind):
    pla_cost = pla_grillon3.gr_cost
    petg_cost = petg_grillon3.gr_cost
    abs_cost = abs_grillon3.gr_cost
    flex_cost = flex_grillon3.gr_cost
    if kind == 'PLA':
        return pla_cost
    elif kind == 'PETG':
        return petg_cost
    elif kind == 'ABS':
        return abs_cost
    elif kind == 'FLEX':
        return flex_cost
    else:
        print('Error Kind_gr_cost')

def cm3_to_gr(kind, cm3=0):
    if kind == 'PLA':
        density = Filament.kind_density['PLA']
        gr = cm3 * density
    elif kind == 'PETG':
        density = Filament.kind_density['PETG']
        gr = cm3 * density
    elif kind == 'ABS':
        density = Filament.kind_density['ABS']
        gr = cm3 * density
    elif kind == 'FLEX':
        density = Filament.kind_density['FLEX']
        gr = cm3 * density
    else:
        print('Kind not found')
    return gr


pla_grillon3 = Filament("PLA", "Grillon3", 1070, spool_gr=1000)
pla_3n3 = Filament("PLA", "3N3", 850, spool_gr=1000)
petg_grillon3 = Filament("PETG", "Grillon3", 1000, spool_gr=1000)
pla_pal = Filament("PLA", "PrintaLot", 960, spool_gr=1000)
flex_grillon3 = Filament("FLEX", "Grillon3", 1500, spool_gr=1000)
abs_grillon3 = Filament("ABS", "Grillon3", 900, spool_gr=1000)

