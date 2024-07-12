import random
import csv

trabajadores = [
    {"nombre": "Juan Pérez"},
    {"nombre": "María García"},
    {"nombre": "Carlos López"},
    {"nombre": "Ana Martínez"},
    {"nombre": "Pedro Rodríguez"},
    {"nombre": "Laura Hernández"},
    {"nombre": "Miguel Sánchez"},
    {"nombre": "Isabel Gómez"},
    {"nombre": "Francisco Díaz"},
    {"nombre": "Elena Fernández"}
]
def asignar_sueldos():
    for empleado in trabajadores:
        empleado['sueldo'] = random.randint(300000, 2500000)


def clasificar_sueldos():
    menor_800k = []
    entre_800k_2m = []
    mayor_2m = []

    for empleado in trabajadores:
        if empleado['sueldo'] < 800000:
            menor_800k.append(empleado)
        elif 800000 <= empleado['sueldo'] <= 2000000:
            entre_800k_2m.append(empleado)
        else:
            mayor_2m.append(empleado)

    print("1. Sueldos menores a $800.000 TOTAL:", len(menor_800k))
    print("2. Sueldos entre $800.000 y $2.000.000 TOTAL:", len(entre_800k_2m))
    print("3. Sueldos superiores a $2.000.000 TOTAL:", len(mayor_2m))

    print("\nSueldos menores a $800.000")
    print("Nombre empleado\t\t\tSueldo")
    for emp in menor_800k:
        print(f"{emp['nombre']}\t\t${emp['sueldo']}")

    print("\nSueldos entre $800.000 y $2.000.000")
    print("Nombre empleado\t\t\tSueldo")
    for emp in entre_800k_2m:
        print(f"{emp['nombre']}\t\t${emp['sueldo']}")

    print("\nSueldos superiores a $2.000.000")
    print("Nombre empleado\t\t\tSueldo")
    for emp in mayor_2m:
        print(f"{emp['nombre']}\t\t${emp['sueldo']}")

def ver_estadisticas():
    total_sueldos = sum(emp['sueldo'] for emp in trabajadores)
    print(f"\nTOTAL SUELDOS: ${total_sueldos}")

def generar_reporte():
    with open('reporte_sueldos.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Nombre empleado',  'Sueldo Base', 'Descuento Salud', 'Descuento AFP', 'Sueldo Líquido'])
        
        for emp in trabajadores:
            salud = emp['sueldo'] * 0.07
            afp = emp['sueldo'] * 0.12
            sueldo_liquido = emp['sueldo'] - salud - afp
            
            writer.writerow([emp['nombre'], emp['sueldo'], salud, afp, sueldo_liquido])

def main():
    print("Bienvenido a doc tops")
    while True:
        print("\nMENU:")
        print("1. Asignar sueldos aleatorios")
        print("2. Clasificar sueldos")
        print("3. Ver estadísticas")
        print("4. Generar reporte de sueldos")
        print("5. Salir del programa")
        
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            asignar_sueldos()
            print("Sueldos aleatorios asignados.")
        elif opcion == '2':
            clasificar_sueldos()
        elif opcion == '3':
            ver_estadisticas()
        elif opcion == '4':
            generar_reporte()
            print("Reporte de sueldos generado en reporte_sueldos.csv")
        elif opcion == '5':
            print("Finalizando programa...")
            print("Desarrollado por Matias Navarrete")
            print("RUT 21.812.606-5")
            break
        else:
            print("eligue una opcion valida")

if __name__ == "__main__":
    main()
