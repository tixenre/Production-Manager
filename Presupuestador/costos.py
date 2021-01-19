costo_luz= 0.036
costo_depreciacion = 0.341
costo_fijo = 0.612
costo_filamento = 1.113

tiendanube_comision = 0.01
mercadopago_comision = 0.0549*1.21
ahora18 = comision = 0.135

comisiones= tiendanube_comision+mercadopago_comision

valorHs = (costo_luz+costo_depreciacion+costo_fijo)*60
valor_hs_mayorista = (costo_luz+costo_depreciacion)*60
valorGr = costo_filamento


def hs_v(hs):
    y1=2 #%
    y2=0.8
    y3=0.4
    y4=0.10

    x1=0 #hs
    x2=7  
    x3=24*1
    x4=24*10
        
    #(y2-y1)/(x2-x1))*VARIABLE INDEPENDIENTE+(y2-(((y2-y1)/(x2-x1))*x2))

    if hs < x2:
        return ((y2-y1)/(x2-x1))*hs+(y2-(((y2-y1)/(x2-x1))*x2))
    elif hs < x3:
        return ((y3-y2)/(x3-x2))*hs+(y3-(((y3-y2)/(x3-x2))*x3))
    elif hs < x4:
        return ((y4-y3)/(x4-x3))*hs+(y4-(((y4-y3)/(x4-x3))*x4))
    else:
        return y4

def gr_v(gr):
    y1=2 #%
    y2=0.7
    y3=0.35
    y4=0.10
        
    gr1=0 #gr
    gr2=50  
    gr3=500
    gr4=5000

    if (gr < gr2):
        return ((y2-y1)/(gr2-gr1))*gr+(y2-(((y2-y1)/(gr2-gr1))*gr2))
    elif (gr < gr3):
        return ((y3-y2)/(gr3-gr2))*gr+(y3-(((y3-y2)/(gr3-gr2))*gr3))
    elif (gr < gr4):
        return ((y4-y3)/(gr4-gr3))*gr+(y4-(((y4-y3)/(gr4-gr3))*gr4))
    else:
        return y4

def gasto(hs,gr):
    gasto = (valorHs*hs+valorGr*gr)
    return gasto

def tiendanube (hs,gr):
    impresion = (gasto(hs,gr)+(hs*hs_v(hs)*valorHs)+(gr*gr_v(gr)*valorGr))/(1-comisiones)+20
    return impresion

def ganancia (hs,gr):
    tiendanube_valor =(tiendanube(hs,gr)*(1-comisiones))
    gasto_valor = gasto(hs,gr)
    ganancia= tiendanube_valor-gasto_valor
    return ganancia

