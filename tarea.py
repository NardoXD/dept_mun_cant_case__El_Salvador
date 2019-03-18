import psycopg2

conexion = psycopg2.connect("dbname=postgres user=postgres")
cur = conexion.cursor()

auxiliar = dict()
datos = dict()
datos2 = dict()

cur.execute('select departamento, municipio, canton, caserio from lpr order by departamento;')

for elem in cur:
    if elem[0] not in datos.keys():
        datos[elem[0]] = dict()
        if elem[1] not in datos[elem[0]].keys():
            datos[elem[0]][elem[1]] = dict()
            if elem[2] not in datos[elem[0]][elem[1]].keys():
                datos[elem[0]][elem[1]][elem[2]] = [elem[3]]
            else:
                datos.update({datos[elem[0]][elem[1]][elem[2]]: datos[elem[0]][elem[1]][elem[2]].append(elem[2])})
    else:
        if elem[1] not in datos[elem[0]].keys():
            datos[elem[0]][elem[1]] = dict()
            if elem[2] not in datos[elem[0]][elem[1]].keys():
                datos[elem[0]][elem[1]][elem[2]] = [elem[3]]
            else:
                datos.update({datos[elem[0]][elem[1]][elem[2]]: datos[elem[0]][elem[1]][elem[2]].append(elem[2])})

counter = 0
for elem in datos.keys():
    print('DEPARTAMENTO: {}\nCANTIDAD MUNICIPIOS: {}'.format(elem, len(datos[elem].keys())))
    counter += len(datos[elem].keys())

print(counter)
