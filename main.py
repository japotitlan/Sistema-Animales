from metodos import *
import subprocess

subprocess.run('cls', shell=True) # Limpiar pantalla (ClearScreen)

def menu():
    
    print("""[Sistema de gestion de animales en un zoologico]
    [1] Ver Animales
    [2] Vacunas
    [3] Paseos
    [4] Alimentación
    [5] Administrar
    [0] Salir""")
    
    opcion = int(input("\nIngrese una opcion: "))
    
    while opcion != 0:

        if opcion == 1: #MOSTRAR ANIMALES REGISTRADOS
            subprocess.run('cls', shell=True)
            verAnimales()
            input("\nEnter Para Continuar...")
            
        elif opcion == 2: #VACUNAR ANIMALES REGISTRADOS
            subprocess.run('cls', shell=True)
            vacunas()
            input("\nEnter Para Continuar...")

        elif opcion == 3: #PASEAR ANIMALES REGISTRADOS
            subprocess.run('cls', shell=True)
            paseos()
            input("\nEnter Para Continuar...")
            
        elif opcion == 4: #ALIMENTAR ANIMALES REGISTRADOS
            subprocess.run('cls', shell=True)
            alimentacion()
            input("\nEnter Para Continuar...")
        
        elif opcion == 5: #REGISTRAR O ELIMINAR ANIMALES
            subprocess.run('cls', shell=True)
            administrar()
            input("\nEnter Para Continuar...")

        else:
            input("Opcion Invalida\nEnter Para Continuar...")

        subprocess.run('cls', shell=True)

        print()
        menu()
        opcion = int(input("\nIngrese una opcion: "))

def login():
    print("""[Sistema de gestion de animales en un zoologico]
             [LOGIN]""")
    user = input("Usuario: ")
    password = input("Contraseña: ")

    if(user == "root" and password == "root"):
        subprocess.run('cls', shell=True)
        menu()
    else:
        input("Credenciales incorrectas...\nEnter para continuar")
        subprocess.run('cls', shell=True)
        login()

login()  