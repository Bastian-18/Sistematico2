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


pila = Pila()

def llegada_paciente(nombre, motivo):
    paciente = {"nombre": nombre, "motivo": motivo}
    cola_pacientes.append(paciente)
    print(f"🩺 Paciente agregado: {nombre} - Motivo: {motivo}")
    agregar_historial([nombre, motivo])

def agregar_historial(historial):
  pila.agregar(historial)
