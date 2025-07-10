import random
import time

# Definimos la clase que representa un nodo en el sistema distribuido
class Node:
    def __init__(self, id):
        self.id = id            # Identificador del nodo
        self.role = "Follower"  # Rol inicial (puede ser Follower, Candidate o Leader)
        self.votes = 0          # Votos recibidos
        self.term = 0           # Término actual (versión de la elección)
        self.alive = True       # Estado del nodo (activo o fallado)

    # Método para iniciar una elección (fase principal de Raft)
    def start_election(self, nodes):
        self.term += 1
        self.votes = 1  # Vota por sí mismo
        self.role = "Candidate"
        print(f"Nodo {self.id} inicia elección (término {self.term})")

        # Solicita votos de los demás nodos activos
        for node in nodes:
            if node.id != self.id and node.alive:
                # Si el término del nodo votante es igual o menor, vota
                if node.term <= self.term:
                    self.votes += 1

        # Si consigue mayoría de votos, se convierte en líder
        if self.votes > len(nodes) // 2:
            self.role = "Leader"
            print(f"Nodo {self.id} es elegido líder (término {self.term})")
        else:
            print(f"Nodo {self.id} no ganó la elección")

# Función principal que simula el entorno distribuido con fallos
def simulate():
    # Creamos 3 nodos
    nodes = [Node(i) for i in range(3)]

    # Simulamos la falla del nodo 0
    nodes[0].alive = False
    print("Nodo 0 ha fallado")

    # Nodo 1 inicia el proceso de elección
    nodes[1].start_election(nodes)

    # Nodo 2 reconoce al líder si se elige exitosamente
    if nodes[1].role == "Leader":
        print(f"Nodo 2 reconoce a Nodo 1 como líder")

# Ejecutamos la simulación
simulate()
