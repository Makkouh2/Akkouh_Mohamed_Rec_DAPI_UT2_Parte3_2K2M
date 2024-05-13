import csv
def calculate_grade(practica01, practica02, practica03, examen,recuperacion, actitud):
    """Funcion me calcula la nota final de cada alumno
        
        parametros:
        - (practica01, practica02, practica03, examen,recuperacion, actitud) variables de que contien el archivo csv 

        salida:
        - La función devuelve un float con la nota final resultante y un booleano con el valor True si el/la alumno/a ha aprobado o el valor False si el/la alumno/a ha suspendido.
        """
    notafinal = ((practica01 + practica02 + practica03) / 3) * 0.3 + max(examen, recuperacion) * 0.6 + actitud * 0.1
    aprobado = notafinal>= 5
    return notafinal, aprobado


archivo_csv= "archivo.csv"
with open (archivo_csv,"r") as file:
    x = csv.reader(file)
    next(x)
    for linea in x:
        practica01 = float(linea[2].replace(',', '.'))
        practica02 = float(linea[3].replace(',', '.'))
        practica03 = float(linea[4].replace(',', '.'))
        examen = float(linea[5].replace(',', '.'))
        recuperacion = float(linea[6].replace(',', '.'))
        actitud = float(linea[7].replace(',', '.'))


        notafinal, aprobado = calculate_grade(practica01, practica02, practica03, examen, recuperacion, actitud)
        print("nota final",notafinal)
        print("aprobado", aprobado)
    