# Paxos-y-Raft


# 🗳️ Simulación de Consenso Distribuido con Raft

Este proyecto implementa una simulación sencilla del algoritmo **Raft** en Python, como parte de la Semana 12 del curso de Sistemas Distribuidos. Se ilustran los conceptos de elección de líder, tolerancia a fallos y replicación de decisiones entre nodos.

## 📌 Descripción

- Tres nodos simulados (objetos en Python)
- Cada nodo puede ser Follower, Candidate o Leader
- Simulación de elección de líder
- Simulación de fallo en un nodo
- Log de eventos que muestra cómo se mantiene el consenso


## ⚙️ Requisitos

- Python 3.7 o superior

No se requieren librerías externas. Solo se usan módulos estándar como `random` y `time`.

## ▶️ Ejecución

1. Clona el repositorio:
   ```bash
   git clone https://github.com/sjmr0911/Paxos-y-Raft.git
   cd Paxos-y-Raft

