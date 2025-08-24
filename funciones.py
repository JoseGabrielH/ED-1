# ordenamiento de lista (solo ordena la lista)
def ordenamiento_burbuja(list):
    n = len(list)
    for i in range(n):
        for j in range(0,n-i-1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]

# ordena la matriz completa
def ordenamiento_columnas(lista):
    # aplana la matriz [9,8,7,6,5,4,3,2,1] lista = [num for fila in matriz for num in fila]
    
    # ordena la lista [1,2,3,4,5,6,7,8,9]
    ordenamiento_burbuja(lista)

    # convierte la lista de nuevo en matriz
    matriz_ordenada = [lista[i:i+columnas] for i in range(0, len(lista), columnas)]

    for fila in matriz_ordenada:
        print("  ",fila)


filas = int(input("Ingrese las filas:"))
columnas = int(input("Ingrese las columnas: "))

lista = []

print("Ingresa los valores de la matriz: ")
for i in range(filas * columnas):
    n = (input())
    lista[i] = n

print("-----Matriz ordenada-----")
ordenamiento_columnas(lista)
