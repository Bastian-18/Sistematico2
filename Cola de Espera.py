# 1.  Simular la llegada de pacientes al centro de salud: o Cada paciente se forma en una cola de espera con su nombre y motivo de consulta

from collections import deque

# Cola para los pacientes en espera
cola_pacientes = deque()

# Función para simular la llegada de un paciente
def llegada_paciente(nombre, motivo):
    paciente = {"nombre": nombre, "motivo": motivo}
    cola_pacientes.append(paciente)
    print(f"🩺 Paciente agregado: {nombre} - Motivo: {motivo}")
  

# Función para ver la cola de espera
def ver_cola():
    print("\n📋 Cola de espera actual:")
    if not cola_pacientes:
        print("No hay pacientes en la cola.")
    else:
        for idx, paciente in enumerate(cola_pacientes, start=1):
            print(f"{idx}. {paciente['nombre']} - {paciente['motivo']}")

# Simulación de llegada de pacientes
llegada_paciente("Ana López", "Dolor de cabeza")
llegada_paciente("Carlos Pérez", "Fiebre")
llegada_paciente("Lucía Ramírez", "Chequeo general")

# Mostrar la cola actual
ver_cola()
