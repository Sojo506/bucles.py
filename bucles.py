f = "s"

while f == "s":
    print("Seleccionar ejercicio")
    control = int(input(
        "\n\tTabla de ejercicios\n(1) (2) (3) (4) (5) (6) (7) (8) (9) (10) (11)\n --> "))

    if control == 1:
        lista = list(range(1, 51))

        for i in lista:
            print(i, end="-")

    elif control == 2:
        lista = list(range(1, 11))
        print("\nLista original")
        for i in lista:
            print(f"{i}", end=" ")

        a = int(input("\nValor numérico --> "))
        print(f"\nNueva lista multiplicada por {a}")

        for i in lista:
            i *= a
            print(i, end=" ")

    elif control == 3:
        lista = []
        salir = False
        while not salir:
            num = int(input("número --> "))
            if num == 0:
                salir = True
            else:
                lista.append(num)

        lista.sort()
        print(f"Lista ordenada \n{list(set(lista))}")

    elif control == 4:
        print("\nSuma de número pares por rango")
        a = int(input("desde --> "))
        b = int(input("hasta --> "))
        suma = 0
        for i in range(a, b+1):
            if i % 2 == 0:
                suma += i
        print(f"total: {suma}")

    elif control == 5:
        # Programa que calcule el factorial de un num entero positivo
        a = int(input("\nNúmero --> "))
        while a < 0:
            print("\nEl número tiene que ser positivo maquinola")
            a = int(input("Número --> "))
        # calcular factorial
        fac = a
        for i in range(a-1, 1-1, -1):
            fac *= i
        print(f"Factorial de {a} --> {fac}")

    elif control == 6:
        print("\nTabla de multiplicar")
        a = int(input("Número --> "))
        lista = []
        # Hacer tabla de multiplicar
        print(f"Tabla del {a}\n")
        for i in range(1, 11):
            lista.append(i*a)
        print(f"tabla del {a} --> {lista}")

    elif control == 7:
        print("\t.:Juego adivina el número:.")
        import random
        aleatorio = random.randint(0, 100)
        # print(numAl)
        salir = False
        intentos = 0
        while not salir:
            userNum = int(input("\nAdivinar --> "))
            if userNum == aleatorio:
                print("\nLo adivinaste!")
                if intentos == 0:
                    print("Genial, lo hiciste al primer intento")
                    salir = True
                else:
                    print(f"intentos --> {intentos}")
                    salir = True
            elif userNum > aleatorio and userNum < 101:
                print("\tdisminuye")
                print("Volver a intentar")
            elif userNum < aleatorio and userNum < 101:
                print("\taumenta")
                print("Volver a intentar")
            else:
                print("\nNúmero fuera de rango (0 al 100)")
                print("Volver a intentar")

            intentos += 1

    elif control == 8:
        print("\t.:Canjero automático:.")
        saldo = 1000
        while True:
            opc = int(input(
                "\n\tOpciones\n(1)Ingresar dinero en la cuenta (2)Retirar dinero de la cuenta\n(3)Mostrar dinero disponible (4)Salir\n\t--> "))

            if opc == 1:
                ingDin = int(input("\nIngresar dinero --> "))
                saldo += ingDin
                print(f"Saldo en la cuenta {saldo}")
            elif opc == 2:
                retDin = int(input("\nRetirar dinero de la cuenta --> "))
                if retDin > saldo:
                    print("No dispones de los fondos suficientes")

                elif retDin < saldo:
                    saldo -= retDin
                    print(f"Retiro exitoso\tSaldo disponible: {saldo}")

            elif opc == 3:
                print(f"Saldo en la cuenta {saldo}")

            elif opc == 4:
                print("Gracias por usar tu cajero automático!")
                break
            else:
                print("Error; valor incorrecto")
    elif control == 9:
        frase = input("Phrase --> ")
        nFrase = ""

        for i in frase:
            if i != " ":
                nFrase += i

        frase = nFrase
        print(f"\nFrase sin espacios: {frase}")
        print(f"n° de caracteres: {len(frase)}")

    elif control == 10:
        cadena = input("\nCaracteres aleatorios: ")
        lista = []

        for i in cadena:
            if i not in lista:
                lista.append(i)   
        
        print(f"Sin caracteres repetidos: {lista}")
    elif control == 11:
        print("\t.:Your phone:.")
        contactos = {}
        while True:
            opc = int(input("\n\tNavegación\n(1)Nuevo contacto (2)Borrar contacto\n(3)Ver contactos existentes (4)Salir\n--> "))
            if opc == 1:
                nombre = input("\nNombre del contacto --> ")
                numero = input("número --> ")
                if nombre not in contactos:
                    contactos [nombre] = numero
                    print("Guardado!")
                else:
                    print("Contacto existente!")
            elif opc == 2:
                print("\n\t.:Borrar contacto:.")
                borrar = input("Escribe el nombre del contacto --> ")
                if borrar in contactos:
                    del(contactos[borrar])
                    print(f"Contacto eliminado: {borrar}")
                elif borrar not in contactos:
                    print("Contacto no existente")
                else:
                    print("Error 404")
            elif opc == 3:
                print("\n\t.:Contactos:.")
                for name, phone in contactos.items():
                    print(f"Nombre: {name}, Número: {phone}")
            elif opc == 4:
                print("\n\t.:Bye:.")
                break
            else:
                print("\nError 404")

    else:
        print("\nError; vuelve a intentarlo")

    f = input("\n\n(s)Otro ejercicio (otra tecla)Salir --> ")
