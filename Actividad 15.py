def quick_sort(listas):
    if len(listas) <= 1:
        return listas

    pivote = listas[0]
    menores = [x for x in listas[1:] if x[1]['nombre'] < pivote[1]['nombre']]
    iguales = [x for x in listas if x[1]['nombre'] == pivote[1]['nombre']]
    mayores = [x for x in listas[1:] if x[1]['nombre'] > pivote[1]['nombre']]
    return quick_sort(menores) + iguales + quick_sort(mayores)
Corredores = {}
def menu():
 while True:
    print("MENU")
    print("1.Agregar")
    print("2.Ordenar por nombre")
    print("3.Eliminar listado")
    print("4.Salir")
    op = int(input("ingrese una opcion: "))

    match op:
        case 1:
         cantidad = int(input('Cantidad de Corredores: '))
         for i in range(cantidad):
          while True:
            codigo = int(input("ingrese numero de dorsal"))
            if codigo < 0:
                print("Agrega el numero")
            elif codigo in Corredores:
             print("ya Utilizado")
            else:
                break
          Corredores[codigo] = {}
          while True:
              try:
                  nombre = input("ingrese el nombre del corredor: ")
                  if nombre == "":
                      print("no puede quedar vacio")
                  else:
                      Corredores[codigo]['nombre'] = nombre
                      break
              except ValueError:
                  print("mira el nombre")
          while True:
            edad = int(input("Ingrese la edad del corredor: "))
            if edad < 0:
                print("no puede ser negativo o no puede quedar vacio")
            else:
                Corredores[codigo]['edad'] = edad
                break
            rango = input("Ingrese la rango del corredor: (Juvenil, Adulto, Master) ")
        case 2:
         print("\n Listado")
         lista = list(Corredores.items())
         ordenados = quick_sort(lista)

         for nombre, valor in ordenados:
             print(f"Dorsal: {nombre}, Datos{valor}")
        case 3:
            sino = input("Desea eliminar todo el listado de corredores? (si o no)")
            if sino == "no":
             return menu()
            else:
                 sisi= input("esta seguro?(si o no)")
                 if sisi == "si":
                     print("\n Yo te pregunte")

        case 4:
            print("Hasta que nos volvamos a ver :3 ")
            break
        case _:
            print("verifica lo ingresado")
            break
menu()