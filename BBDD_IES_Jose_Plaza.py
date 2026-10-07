#Tengo guardado en diccionarios datos de varios alumnos matriculados en un instituto ficticio
alumno1 = {
    "nombre": "Jose",
    "DNI": "12345678R",
    "edad": 20,
    "ciudad": "Jaén",
    "FP": "ASIR"
}

alumno2 = {
    "nombre": "Nerea",
    "DNI": "45678901S",
    "edad": 22,
    "ciudad": "Linares",
    "FP": "DAM"
}

alumno3 = {
    "nombre": "Luis",
    "DNI": "23456789N",
    "edad": 21,
    "ciudad": "Bailen",
    "FP": "ASIR"
}

alumno4 = {
    "nombre": "Paula",
    "DNI": "78901234V",
    "edad": 25,
    "ciudad": "Guarroman",
    "FP": "DAW"
}

#El programa nos da la bienvenida a la Base de datos del instituto y nos pide un DNI para consultar datos de cualquier alumno
print("Bienvenido a la BBDD del IES Jose Plaza")
print("Indique el DNI del alumno")

#Mientras dure el programa nos pide el DNI de los alumnos matriculados
while True:

    dni = str(input("#> "))

    if dni == alumno1['DNI']:
        for conf in alumno1.items():
            print(conf)

    elif dni == alumno2['DNI']:
        for conf in alumno2.items():
            print(conf)

    elif dni == alumno3['DNI']:
        for conf in alumno3.items():
            print(conf)

    elif dni == alumno4['DNI']:
        for conf in alumno4.items():
            print(conf)

    #Si introducimos un DNI que no coincide, el programa termina indicando que el DNI no es valido o esta en la base de datos
    else:
        print("El DNI que has introducido no es valido o no esta incluido en la BBDD")
        break
