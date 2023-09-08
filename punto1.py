# SIERRA MUNERA JUAN SEBASTIAN
# OCHOA RESTREPO JUAN CAMILO

estudiantes = {}

opcion = 1
while opcion ==1 or opcion == 2 or opcion == 3 or opcion == 4 :
    opcion = int(input(("Escoga una opción para continuar: \n1.Agregar \n2.Actualizar \n3.Consultar \n4.Eliminar \n5.Salir \n\n")))
    if opcion == 1:
      nombre = input("Nombre:  ")
      apellido = input("Apellido: ")
      edad = int(input("Edad:"))
      estudiantes['nombre'] = nombre
      estudiantes['apellido'] = apellido
      estudiantes['edad'] = edad
    elif opcion == 2:
      nombre = input("Nombre:  ")
      apellido = input("Apellido: ")
      edad = int(input("Edad:"))
      estudiantes['nombre'] = nombre
      estudiantes['apellido'] = apellido
      estudiantes['edad'] = edad
    elif opcion == 3:
      print(estudiantes)
    elif opcion == 4:
      del estudiantes[nombre]
    elif opcion == 5:
        break
while opcion !=1 and opcion !=2 and opcion !=3 and opcion !=4 and opcion !=5:
        print("Opcion Invalida")
        opcion = int(input(("Escoga una opción para continuar: \n1.Agregar \n2.Actualizar \n3.Consultar \n4.Eliminar \n5.Salir \n\n")))
        if opcion == 5:
            break

