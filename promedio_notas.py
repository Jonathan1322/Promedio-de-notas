def mostrar_menu():
    print("--- MENÚ ---")
    print("1. Ingresar notas del estudiante")
    print("2. Calcular promedio")
    print("3. Verificar si aprobó la materia")
    print("4. Salir")


def ingresar_notas():
    global notas
    notas = []
    cantidad = int(input("¿Cuántas notas deseas ingresar? "))
    for i in range(cantidad):
        nota = float(input(f"Ingrese la nota #{i+1}: "))
        notas.append(nota)
    print("Notas guardadas correctamente.")


def calcular_promedio():
    if not notas:
        print("Primero debes ingresar las notas.")
        return None
    promedio = sum(notas) / len(notas)
    print(f"El promedio de las notas es: {promedio:.2f}")
    return promedio


def verificar_aprobacion():
    promedio = calcular_promedio()
    if promedio is not None:
        if promedio >= 3.0:
            print("(☞ﾟヮﾟ)☞ El estudiante APROBÓ la materia.")
        else:
            print("(T_T) El estudiante REPROBÓ la materia.")



notas = []
while True:
    mostrar_menu()
    opcion = input("Seleccione una opción (1-4): ")

    if opcion == '1':
        ingresar_notas()
    elif opcion == '2':
        calcular_promedio()
    elif opcion == '3':
        verificar_aprobacion()
    elif opcion == '4':
        print("Saliendo del programa...")
        break
    else:
        print("Opción inválida. Por favor, elige entre 1 y 4.")
