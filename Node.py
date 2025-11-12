class Node:
    def __init__(self, name):
        self.name = name
        self.next = None
        self.prev = None
        self.sublista = []

class MultiLista:
    def __init__(self):
        self.cabeza = None
    
    def insertar(self, name):
        """Inserta un nodo al inicio de la multilista"""
        nuevo_nodo = Node(name)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
        else:
            nuevo_nodo.next = self.cabeza
            self.cabeza.prev = nuevo_nodo
            self.cabeza = nuevo_nodo
    
    def agregar_sublista(self, name, elemento):
        """Agrega un elemento a la sublista de un nodo"""
        nodo = self._buscar_nodo(name)
        if nodo:
            nodo.sublista.append(elemento)
    
    def _buscar_nodo(self, name):
        """Busca un nodo por nombre"""
        actual = self.cabeza
        while actual:
            if actual.name == name:
                return actual
            actual = actual.next
        return None
    
    def mostrar(self):
        """Muestra todos los nodos y sus sublistas"""
        actual = self.cabeza
        while actual:
            print(f"Nodo: {actual.name}, Sublista: {actual.sublista}")
            actual = actual.next

ml = MultiLista()
ml.insertar("Nodo1")
ml.insertar("Nodo2")
ml.agregar_sublista("Nodo1", "Elemento1")
ml.agregar_sublista("Nodo1", "Elemento2")
ml.agregar_sublista("Nodo2", "ElementoA")
ml.mostrar()