dependencias = {}

factor_emision_electricidad_tibu = 0.6
factor_emision_transport_tibu = 0.3  

def registrar_dependencia():
    nombre_dependencia = input("Ingrese el nombre de la dependencia: ")
    dependencias[nombre_dependencia] = {"consumo_electricidad": 0, "consumo_transport": 0}

def registrar_consumo_dependencia():
    nombre_dependencia = input("Ingrese el nombre de la dependencia: ")
    if nombre_dependencia in dependencias:
        dependencias[nombre_dependencia]["consumo_electricidad"] += float(input("Consumo de electricidad en kWh: "))
        dependencias[nombre_dependencia]["consumo_transport"] += float(input("Consumo de transporte en km: "))
    else:
        print("La dependencia no ha sido registrada.")

def calcular_co2_dependencia(consumo):
    emision_electricidad = consumo["consumo_electricidad"] * factor_emision_electricidad_tibu
    emision_transport = consumo["consumo_transport"] * factor_emision_transport_tibu
    return emision_electricidad + emision_transport

def calcular_co2_total():
    total_co2 = 0
    for dependencia, consumo in dependencias.items():
        total_co2 += calcular_co2_dependencia(consumo)
        print(f"CO2 producido por {dependencia}: {calcular_co2_dependencia(consumo)} tCO2eq")
    return total_co2


def dependencia_mayor_co2():
    max_co2 = 0
    dependencia_max_co2 = ""
    for dependencia, consumo in dependencias.items():
        total_co2 = calcular_co2_dependencia(consumo)
        if total_co2 > max_co2:
            max_co2 = total_co2
            dependencia_max_co2 = dependencia
    return dependencia_max_co2


def menu():
    while True:
        print(">Menú Principal:")
        print("1. Registrar Dependencia")
        print("2. Registrar consumo por dependencia")
        print("3. Ver CO2 producido")
        print("4. Dependencia que produce mayor CO2")
        print("5. Salir")

        opcion = input("Ingrese el número de la opción deseada: ")

        if opcion == "1":
            registrar_dependencia()
        elif opcion == "2":
            registrar_consumo_dependencia()
        elif opcion == "3":
            total_co2 = calcular_co2_total()
            print(f"\nTotal CO2 producido: {total_co2} tCO2eq")
        elif opcion == "4":
            dependencia_max_co2 = dependencia_mayor_co2()
            print(f"\nLa dependencia que produce mayor CO2 es: {dependencia_max_co2}")
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Por favor, ingrese un número válido.")

# Llamada a la función del menú principal
menu()