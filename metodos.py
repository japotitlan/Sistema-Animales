import datetime

#
# DICCIONARIOS DE ANIMALES
#
mamiferos = [{
    "nombre": "raul",
    "edad": 3,
    "peso": 12,
    "especie": "gato",
    "vacuna": "2018-04-11",
    "paseo": "2022-10-13 08:00:00",
    "comida": "2022-10-13 08:00:00"
    },
    {
    "nombre": "michum",
    "edad": 2,
    "peso": 10,
    "especie": "gato",
    "vacuna": "2017-11-02",
    "paseo": "2022-10-13 08:00:00",
    "comida": "2022-10-13 08:00:00"
    },
    {
    "nombre": "firo",
    "edad": 8,
    "peso": 23,
    "especie": "perro",
    "vacuna": "2020-02-04",
    "paseo": "2022-10-13 08:00:00",
    "comida": "2022-10-13 08:00:00"
    }
]

acuaticos = [{
    "nombre": "junki",
    "edad": 5,
    "peso": 40,
    "especie": "delfin",
    "vacuna": "2018-04-11",
    "paseo": "2022-10-13 08:00:00",
    "comida": "2022-10-13 08:00:00"
    },
    {
    "nombre": "tortin",
    "edad": 99,
    "peso": 112,
    "especie": "tortuga",
    "vacuna": "2018-04-11",
    "paseo": "2022-10-13 08:00:00",
    "comida": "2022-10-13 08:00:00"
    },
    {
    "nombre": "mari",
    "edad": 2,
    "peso": 72,
    "especie": "foca",
    "vacuna": "2018-04-11",
    "paseo": "2022-10-13 08:00:00",
    "comida": "2022-10-13 08:00:00"
    }
]

avez = [{
    "nombre": "peter",
    "edad": 2,
    "peso": .600,
    "especie": "perico",
    "vacuna": "2018-04-11",
    "paseo": "2022-10-13 08:00:00",
    "comida": "2022-10-13 08:00:00"
    },
    {
    "nombre": "caritas",
    "edad": 3,
    "peso": .400,
    "especie": "guacamaya",
    "vacuna": "2018-04-11",
    "paseo": "2022-10-13 08:00:00",
    "comida": "2022-10-13 08:00:00"
    },
    {
    "nombre": "teflon",
    "edad": 4,
    "peso": .900,
    "especie": "cuervo",
    "vacuna": "2018-04-11",
    "paseo": "2022-10-13 08:00:00",
    "comida": "2022-10-13 08:00:00"
    }
]

##############################################################################################

def tiposAnimales():               # MENU PARA SELECCIONAR EL TIPO DE ANIMALES A MOSTRAR
    print("""\n[Tipos de Animales]
    [1] Mamiferos
    [2] Acuaticos
    [3] Avez
    [0] Regresar..""")

def verAnimales():                 # MOSTRAR CADA OBJETO DEL DICCIONARIO
    tiposAnimales()
    op = int(input("\nIngrese una opcion: "))
    print()

    while op != 0: 
        if op == 1:                    # MOSTRAR MAMIFEROS
            if len(mamiferos) > 0:
                for mamifero in mamiferos:
                    print(f"Nombre: {mamifero['nombre']}, Edad: {mamifero['edad']}, Peso: {mamifero['peso']}kg, Especie: {mamifero['especie']}, Ultima Vacuna: {mamifero['vacuna']}, Ultimo Paseo: {mamifero['paseo']}, Ultima Comida: {mamifero['comida']}")
            else:
                print("No se encontraron registros...")
        
        elif op == 2:                  # MOSTRAR ACUATICOS
            if len(acuaticos) > 0:
                for acuatico in acuaticos:
                    print(f"Nombre: {acuatico['nombre']}, Edad: {acuatico['edad']}, Peso: {acuatico['peso']}kg, Especie: {acuatico['especie']}, Ultima Vacuna: {acuatico['vacuna']}, Ultimo Paseo: {acuatico['paseo']}, Ultima Comida: {acuatico['comida']}")
            else:
                print("No se encontraron registros...")
        
        elif op == 3:                  # MOSTRAR AVEZ
            if len(avez) > 0:
                for ave in avez:
                    print(f"Nombre: {ave['nombre']}, Edad: {ave['edad']}, Peso: {ave['peso']}kg, Especie: {ave['especie']}, Ultima Vacuna: {ave['vacuna']}, Ultimo Paseo: {ave['paseo']}, Ultima Comida: {ave['comida']}")
            else:
                print("No se encontraron registros...")

        input("\nEnter Para Continuar...")## PA QUE SE REPITA EL BUCLE        
        tiposAnimales()
        op = int(input("\nIngrese una opcion: "))
        print()

##############################################################################################

#       VACUNAR   ######################

fechaActual = datetime.date.today()

def vacunas():
    print("Vacunacion para animales")

    tiposAnimales()
    op = int(input("\nIngrese una opcion: "))
    print()

    if op == 1: 
        if len(mamiferos) > 0:
            for mamifero in mamiferos:
                print(f"Nombre: {mamifero['nombre']}, Edad: {mamifero['edad']}, Peso: {mamifero['peso']}kg, Especie: {mamifero['especie']}, Ultima Vacuna: {mamifero['vacuna']}, Ultimo Paseo: {mamifero['paseo']}, Ultima Comida: {mamifero['comida']}")

            aVacunar = input("\nIngrese el nombre exacto del animal a vacunar: ")

            for mamifero in mamiferos:
                if aVacunar == mamifero['nombre']:
                    mamifero.update({'vacuna': fechaActual})      
        else:
            print("No se encontraron registros...")
        
    elif op == 2:
        if len(acuaticos) > 0:
            for acuatico in acuaticos:
                print(f"Nombre: {acuatico['nombre']}, Edad: {acuatico['edad']}, Peso: {acuatico['peso']}kg, Especie: {acuatico['especie']}, Ultima Vacuna: {acuatico['vacuna']}, Ultimo Paseo: {acuatico['paseo']}, Ultima Comida: {acuatico['comida']}")
            
            aVacunar = input("\nIngrese el nombre exacto del animal a vacunar: ")

            for acuatico in acuaticos:
                if aVacunar == acuatico['nombre']:
                    acuatico.update({'vacuna': fechaActual})
        else:
            print("No se encontraron registros...")
        
    elif op == 3:
        if len(avez) > 0:
            for ave in avez:
                print(f"Nombre: {ave['nombre']}, Edad: {ave['edad']}, Peso: {ave['peso']}kg, Especie: {ave['especie']}, Ultima Vacuna: {ave['vacuna']}, Ultimo Paseo: {ave['paseo']}, Ultima Comida: {ave['comida']}")
            
            aVacunar = input("\nIngrese el nombre exacto del animal a vacunar: ")

            for ave in avez:
                if aVacunar == ave['nombre']:
                    ave.update({'vacuna': fechaActual})
        else:
            print("No se encontraron registros...")


#       PASEAR   ######################

x = datetime.datetime.now()
fechaHoraActual = x.strftime("%Y-%m-%d %H:%M:%S")

def paseos():
    print("Pasear a los animales")

    tiposAnimales()
    op = int(input("\nIngrese una opcion: "))
    print()

    if op == 1: 
        if len(mamiferos) > 0:
            for mamifero in mamiferos:
                print(f"Nombre: {mamifero['nombre']}, Edad: {mamifero['edad']}, Peso: {mamifero['peso']}kg, Especie: {mamifero['especie']}, Ultima Vacuna: {mamifero['vacuna']}, Ultimo Paseo: {mamifero['paseo']}, Ultima Comida: {mamifero['comida']}")

            aPasear = input("\nIngrese el nombre exacto del animal a pasear: ")

            for mamifero in mamiferos:
                if aPasear == mamifero['nombre']:
                    mamifero.update({'paseo': fechaHoraActual})      
        else:
            print("No se encontraron registros...")
        
    elif op == 2:
        if len(acuaticos) > 0:
            for acuatico in acuaticos:
                print(f"Nombre: {acuatico['nombre']}, Edad: {acuatico['edad']}, Peso: {acuatico['peso']}kg, Especie: {acuatico['especie']}, Ultima Vacuna: {acuatico['vacuna']}, Ultimo Paseo: {acuatico['paseo']}, Ultima Comida: {acuatico['comida']}")
            
            aPasear = input("\nIngrese el nombre exacto del animal a pasear: ")

            for acuatico in acuaticos:
                if aPasear == acuatico['nombre']:
                    acuatico.update({'paseo': fechaHoraActual})
        else:
            print("No se encontraron registros...")
        
    elif op == 3:
        if len(avez) > 0:
            for ave in avez:
                print(f"Nombre: {ave['nombre']}, Edad: {ave['edad']}, Peso: {ave['peso']}kg, Especie: {ave['especie']}, Ultima Vacuna: {ave['vacuna']}, Ultimo Paseo: {ave['paseo']}, Ultima Comida: {ave['comida']}")
            
            aPasear = input("\nIngrese el nombre exacto del animal a pasear: ")

            for ave in avez:
                if aPasear == ave['nombre']:
                    ave.update({'paseo': fechaHoraActual})
        else:
            print("No se encontraron registros...")

#       ALIMENTAR   ######################

def alimentacion():
    print("Alimentar a los animales")

    tiposAnimales()
    op = int(input("\nIngrese una opcion: "))
    print()

    if op == 1: 
        if len(mamiferos) > 0:
            for mamifero in mamiferos:
                print(f"Nombre: {mamifero['nombre']}, Edad: {mamifero['edad']}, Peso: {mamifero['peso']}kg, Especie: {mamifero['especie']}, Ultima Vacuna: {mamifero['vacuna']}, Ultimo Paseo: {mamifero['paseo']}, Ultima Comida: {mamifero['comida']}")

            alimentar = input("\nIngrese el nombre exacto del animal a alimentar: ")

            for mamifero in mamiferos:
                if alimentar == mamifero['nombre']:
                    mamifero.update({'comida': fechaHoraActual})      
        else:
            print("No se encontraron registros...")
        
    elif op == 2:
        if len(acuaticos) > 0:
            for acuatico in acuaticos:
                print(f"Nombre: {acuatico['nombre']}, Edad: {acuatico['edad']}, Peso: {acuatico['peso']}kg, Especie: {acuatico['especie']}, Ultima Vacuna: {acuatico['vacuna']}, Ultimo Paseo: {acuatico['paseo']}, Ultima Comida: {acuatico['comida']}")
            
            alimentar = input("\nIngrese el nombre exacto del animal a alimentar: ")

            for acuatico in acuaticos:
                if alimentar == acuatico['nombre']:
                    acuatico.update({'comida': fechaHoraActual})
        else:
            print("No se encontraron registros...")
        
    elif op == 3:
        if len(avez) > 0:
            for ave in avez:
                print(f"Nombre: {ave['nombre']}, Edad: {ave['edad']}, Peso: {ave['peso']}kg, Especie: {ave['especie']}, Ultima Vacuna: {ave['vacuna']}, Ultimo Paseo: {ave['paseo']}, Ultima Comida: {ave['comida']}")
            
            alimentar = input("\nIngrese el nombre exacto del animal a alimentar: ")

            for ave in avez:
                if alimentar == ave['nombre']:
                    ave.update({'comida': fechaHoraActual})
        else:
            print("No se encontraron registros...")

##############################################################
## ADMINISTRAR

def adminAnimales():
    print("""\n[Administracion de Animales]
    [1] Registrar
    [2] Eliminar
    [0] Regresar..""")

def administrar():
    tiposAnimales()
    op = int(input("\nIngrese una opcion: "))
    print()

    if op == 1:
        adminAnimales()
        opx = int(input("\nIngrese una opcion: "))
        print()

        if opx == 1:   #REGISTRAR
            print("Registrar Mamifero")
            nombre = input("Nombre: ")
            edad = int(input("Edad: "))
            peso = float(input("Peso: "))
            especie = input("Especie: ")
            vacuna = fechaActual
            paseo = fechaHoraActual
            comida = fechaHoraActual
            mamiferos.append({"nombre":nombre, "edad":edad, "peso":peso, "especie":especie, "vacuna":vacuna, "paseo":paseo, "comida":comida})
            print("Agregado con exito\n")

        elif opx == 2: #ELIMINAR
            contador = 0
            for animal in mamiferos:
                print(f"[{contador}]Nombre: {animal['nombre']}, Especie: {animal['especie']}")
                contador += 1
            
            borrar = int(input("\nNumero de animal a eliminar: "))

            mamiferos.pop(borrar)
            print("Se elimino el registro correctamente..")
    
    elif op == 2:
        adminAnimales()
        opx = int(input("\nIngrese una opcion: "))
        print()

        if opx == 1:   #REGISTRAR
            print("Registrar Acuatico")
            
            nombre = input("Nombre: ")
            edad = int(input("Edad: "))
            peso = float(input("Peso: "))
            especie = input("Especie: ")
            vacuna = fechaActual
            paseo = fechaHoraActual
            comida = fechaHoraActual

            acuaticos.append({"nombre":nombre, "edad":edad, "peso":peso, "especie":especie, "vacuna":vacuna, "paseo":paseo, "comida":comida})

            print("Agregado con exito\n")
        elif opx == 2: #ELIMINAR
            contador = 0
            for animal in acuaticos:
                print(f"[{contador}]Nombre: {animal['nombre']}, Especie: {animal['especie']}")
                contador += 1
            
            borrar = int(input("\nNumero de animal a eliminar: "))

            acuaticos.pop(borrar)
            print("Se elimino el registro correctamente..")
    
    elif op == 3:
        adminAnimales()
        opx = int(input("\nIngrese una opcion: "))
        print()

        if opx == 1:   #REGISTRAR
            print("Registrar Ave")

            nombre = input("Nombre: ")
            edad = int(input("Edad: "))
            peso = float(input("Peso: "))
            especie = input("Especie: ")
            vacuna = fechaActual
            paseo = fechaHoraActual
            comida = fechaHoraActual

            avez.append({"nombre":nombre, "edad":edad, "peso":peso, "especie":especie, "vacuna":vacuna, "paseo":paseo, "comida":comida})

            print("Agregado con exito\n")
        elif opx == 2: #ELIMINAR
            contador = 0
            for animal in avez:
                print(f"[{contador}]Nombre: {animal['nombre']}, Especie: {animal['especie']}")
                contador += 1
            
            borrar = int(input("\nNumero de animal a eliminar: "))

            avez.pop(borrar)
            print("Se elimino el registro correctamente..")

    






####################