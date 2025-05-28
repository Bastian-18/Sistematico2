while True:
    print("\n--- Centro de Salud ---")
    print("1. Ver pacientes en espera")
    print("2. Atender al siguiente paciente")
    print("3. Consultar historial de recetas")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        ver_pacientes_en_espera()
    elif opcion == "2":
        atender_siguiente_paciente()
    elif opcion == "3":
        consultar_historial()
    elif opcion == "4":
        print("Saliendo del sistema...")
        break
    else:
        print("Opción no válida. Intente nuevamente.")