# ordenar matriz
def ordenar_matriz(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0,n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j] # esta parte del codigo agarra una lista y la ordena 
    
    matriz = [lista[i:i+colunmas] for i in range(0, len(lista), colunmas)] # esta parte del codigo convierte la lista en una matriz y la imprime
    for fila in matriz:
        print(fila)    

# este codigo lo que hace es llenar una lista por medio de un for de puros "0" de tamaño filas*columnas, luego llena la lista con los datos que el usuario le da y llama
# a la funcion ordenar_matriz.

filas = int(input("Ingrese filas:"))
colunmas = int(input("Ingrese columnas: "))
print("Ingresa los valores de la matriz: ")

lista = [0 for _ in range(filas * colunmas)]
for i in range(filas*colunmas):
    n = int(input())
    lista[i] =  n

ordenar_matriz(lista)





