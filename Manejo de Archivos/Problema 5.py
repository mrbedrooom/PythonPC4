# GENERA TABLAS DE MULTIPLICAR

def escribir_tabla_multiplicar(n):
    with open(f"tabla-{n}.txt", 'w') as archivo:
        for i in range(1, 11):
            archivo.write(f"{n} x {i} = {n * i}\n")
    print(f"Tabla de multiplicar del {n} guardada en tabla-{n}.txt")

def leer_tabla_multiplicar(n):
    try:
        with open(f"tabla-{n}.txt", 'r') as archivo:
            contenido = archivo.read()
            print(contenido)
    except FileNotFoundError:
        print(f"Error: El archivo tabla-{n}.txt no existe.")

def leer_linea_tabla_multiplicar(n, m):
    try:
        with open(f"tabla-{n}.txt", 'r') as archivo:
            lineas = archivo.readlines()
            if 1 <= m <= 10:
                print(lineas[m - 1].strip())
            else:
                print("Error: El número de línea debe estar entre 1 y 10.")
    except FileNotFoundError:
        print(f"Error: El archivo tabla-{n}.txt no existe.")

def mostrar_menu():
    print("\nMenú:")
    print("1. Escribir tabla de multiplicar")
    print("2. Leer tabla de multiplicar")
    print("3. Leer línea específica de tabla de multiplicar")
    print("4. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("\nElige una opción: ")

        if opcion == '1':
            n = int(input("Introduce un número entero entre 1 y 10: "))
            if 1 <= n <= 10:
                escribir_tabla_multiplicar(n)
            else:
                print("Error: El número debe estar entre 1 y 10.")
        elif opcion == '2':
            n = int(input("Introduce un número entero entre 1 y 10: "))
            if 1 <= n <= 10:
                leer_tabla_multiplicar(n)
            else:
                print("Error: El número debe estar entre 1 y 10.")
        elif opcion == '3':
            n = int(input("Introduce un número entero entre 1 y 10: "))
            m = int(input("Introduce el número de la línea que quieres "+
                          "leer (1-10): "))
            if 1 <= n <= 10:
                leer_linea_tabla_multiplicar(n, m)
            else:
                print("Error: El número debe estar entre 1 y 10.")
        elif opcion == '4':
            print("Saliste del programa.")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()
