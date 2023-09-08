# SIERRA MUNERA JUAN SEBASTIAN
# OCHOA RESTREPO JUAN CAMILO

estudiantes =[]

opcion =1
while opcion ==1 or opcion == 2 or opcion == 3 or opcion == 4:
    opcion = int(input(("Escoga una opción para continuar: \n1.Agregar \n2.Actualizar ultima entrada \n3.Consultar \n4.Eliminar \n5.Salir \n\n")))
    if opcion == 1:
      nombre = input("Nombre: ")
      estudiantes.insert(0,nombre)
    elif opcion == 2:
      nombre = input("Nombre: ")
      estudiantes[0]=nombre
    elif opcion == 3:
      print(estudiantes)
    elif opcion == 4:
      nombre = input("Nombre estudiante a eliminar: ")
      estudiantes.remove(nombre)
    elif opcion == 5:
        break
while opcion !=1 and opcion !=2 and opcion !=3 and opcion !=4 and opcion !=5:
        print("Opcion Invalida")
        opcion = int(input(("Escoga una opción para continuar: \n1.Agregar \n2.Actualizar \n3.Consultar \n4.Eliminar \n5.Salir \n\n")))
        if opcion == 5:
            break   