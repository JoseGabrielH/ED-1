
def ordenamiento_burbuja(list):
    n = len(list)
    for i in range(n):
        for j in range(0,n-i-1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]

filas = 0
columnas = 0
seguir = True

print("Este codigo busca el numero que ingreses dentro de una")
print("matriz previamente ingresada.")

while seguir:
    
    filas = int(input("Cuantas filas?"))
    columnas = int(input("Cuantas columnas?"))

    matriz = [[0 for _ in range(columnas)]for _ in range(filas)]
    matrizz = [[0 for _ in range(columnas)]for _ in range(filas)]
    
    print("Ingrese los valores de la matriz: ")
    for i in range(filas):
        for j in range(columnas):
            n = int(input())
            matriz[i][j] = n

    respuesta = input("Quieres ordenar la matriz? (si/no)")
    if respuesta == "si":
        lista = [num for fila in matriz for num in fila]
        ordenamiento_burbuja(lista)
        matriz_ordenada = [lista[i:i+columnas] for i in range(0, len(lista), columnas)]
        for fila in matriz_ordenada:
            print("                 ",fila)
            n = int(input("Ingrese el numero a buscar y se armara una matriz con la pisicion en la que esta en numero: "))
        for i in range(filas):
            for j in range(columnas):
                if matriz_ordenada[i][j] == n:
                    matrizz[i][j] = n

    print("------------------Matriz ingresada------------------")
    for fila in matriz:
        print("                 ",fila)

    n = int(input("Ingrese el numero a buscar y se armara una matriz con la pisicion en la que esta en numero: "))
    for i in range(filas):
        for j in range(columnas):
            if matriz[i][j] == n:
                matrizz[i][j] = n

    print("------------Matriz con el numero que buscabas--------")
    for fila in matrizz:
        print("                      ",fila)
    
    respuesta = input("De nuevo? (si/no)")
    if respuesta == "si":
        seguir = True
    elif respuesta == "no":
        seguir = False
        print(".......noEste proceso ha finalizado......")