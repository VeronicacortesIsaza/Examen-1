def menu():
    hotel = Hotel()
    while True:
        print("\n===== SISTEMA DE RESERVAS DE HOTEL =====")
        print("1. Reservar habitación")
        print("2. Cancelar reserva")
        print("3. Mostrar reservas")
        print("4. Salir")
        
        while True:
         opcion = input("Elige una opción (1-4): ")
         if opcion.isdigit():  
            opcion = int(opcion)  
            if 1 <= opcion <= 4:
                print("Opción válida:", opcion) 
                break  
            else:
                print("El número debe estar entre 1 y 4.")
         else:
            print("Debes ingresar un número válido.")

        
        if opcion == "1":
            cliente = input("Nombre del cliente: ")
            noches = int(input("Número de noches: "))
            print("Tipos de habitación:")
            print("1. Estándar ($200000/noche)")
            print("2. Suite ($300000/noche)")
            print("3. Premium ($450000/noche)")
            tipo = input("Seleccione tipo: ")

            if tipo == 1:
                hotel.reservar(cliente, noches, HabitacionEstandar)
            elif tipo == 2:
                hotel.reservar(cliente, noches, Suite)
            elif tipo == 3:
                hotel.reservar(cliente, noches, Premium)
            else:
                print("Tipo inválido.")

        elif opcion == 2:
            cliente = input("Ingrese el nombre del cliente para cancelar la reserva: ")
            hotel.cancelar_reserva(cliente)

        elif opcion == 3:
            hotel.mostrar_reservas()

        elif opcion == 4:
            print("Saliendo del sistema...")
            break

        else:
            print("Opción inválida. Intente de nuevo.")

