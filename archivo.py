siguiente = True 

with open("nombres.txt", "w", encoding="utf-8") as f:
        while siguiente:
            f.writelines([input("Nombre completo:"),"\n"])
            respuesta = input("Hay alguie mas en la fila? (si/no)")
            if respuesta == "si":
                siguiente = True
            else:
                siguiente = False
        
with open("nombres.txt", mode="r", encoding="utf-8") as f:
    todo = f.read()
    print("Nombres en la lista:")
    print(todo)