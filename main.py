class Pila:
  def __init__(self):
    self.historial = []

  def agregar(self, elemento):
    self.historial.append(elemento)

  def quitar(self):
    if not self.esta_vacia():
      return self.historial.pop()
    return None

  def mostrar(self):
    return self.historial

  def esta_vacia(self):
    return len(self.historial) == 0

from collections import deque

# Cola para los pacientes en espera
cola_pacientes = deque()
pila = Pila()

def agregar_historial(historial):
  pila.agregar(historial)

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

def consultar_historial(nombre):
    if nombre in historial_recetas and historial_recetas[nombre]:
        print(f"Historial de recetas de {nombre}:")
        for receta in reversed(historial_recetas[nombre]):
            print(f"- {receta}")
    else:
        print(f"No hay recetas registradas para {nombre}.")

def atender_siguiente_paciente():
    if cola_pacientes:
        nombre, motivo = cola_pacientes.popleft()
        print(f"Atendiendo a {nombre} (Motivo: {motivo})")
        receta = input(f"Ingrese la receta para {nombre}: ")
        if nombre not in historial_recetas:
            historial_recetas[nombre] = []
        historial_recetas[nombre].append(receta)
        print(f"Receta registrada correctamente.")
	agregar_historial([nombre, motivo])
    else:
        print("No hay pacientes en espera.")

while True:
    print("\nOpciones:")
    print("1. Ver pacientes en espera")
    print("2. Atender siguiente paciente")
    print("3. Consultar historial de un paciente")
    print("4. Llegada Paciente")
    print("5. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        ver_pacientes_en_espera()
    elif opcion == "2":
        atender_siguiente_paciente()
    elif opcion == "3":
        nombre = input("Ingrese el nombre del paciente: ")
        consultar_historial(nombre)
    elif opcion == "4":
        nombre = input("Ingrese el nombre del paciente: ")
	motivo= input("Motivo de llegada")
	llegada_paciente(nombre, motivo)
    elif opcion =="5"
	print("Saliendo...")
	break
    else:
        print("Opción no válida. Intente de nuevo.")


