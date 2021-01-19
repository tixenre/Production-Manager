import csv
import costos
import math

contador=0

with open('base_datos.csv', 'r') as csv_file:
    csv_data = csv.DictReader(csv_file)
    
    with open('csv_export_test.csv', 'w',newline='') as new_file:
        fieldnames = ["Nombre","Variante","Hs","Gr","Costo","Ganancia","Precio"]

        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter=',')

        csv_writer.writeheader()

        for line in csv_data:
            contador = contador + 1
            nombre_data= line["Nombre"]
            variante_data= line["Variante"]
            hs_data= float(line["Hs"])
            gr_data= float(line["Gr"])
            costo_data=int(costos.gasto(hs_data,gr_data))
            ganancia_data=int(costos.ganancia(hs_data,gr_data))
            tiendanube_data= int(math.ceil(costos.tiendanube(hs_data,gr_data)))
            csv_writer.writerow({"Nombre":nombre_data,
                                "Variante":variante_data,
                                "Hs":hs_data,
                                "Gr":gr_data,
                                "Costo":costo_data,
                                "Ganancia":ganancia_data,
                                "Precio":tiendanube_data})


#for i in data:
#    print(i)