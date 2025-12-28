def main():
    suma_mayor_5 = 0
    contador_mayor_5 = 0

    suma_menor_4 = 0
    contador_menor_4 = 0

    contador_unos = 0
    suma_total = 0

    for i in range(1, 21):
        nota = float(input(f"Ingrese la nota {i} (1 a 7): "))

        # Opción extra: salir si la nota es 0
        if nota == 0:
            print("ERROR: Se ingresó una nota 0. Programa finalizado.")
            return

        # Validación básica
        if nota < 1 or nota > 7:
            print("ERROR: La nota debe estar entre 1 y 7.")
            return

        # Promedio total
        suma_total += nota

        # Promedio mayores a 5
        if nota > 5:
            suma_mayor_5 += nota
            contador_mayor_5 += 1

        # Promedio menores a 4
        if nota < 4:
            suma_menor_4 += nota
            contador_menor_4 += 1

        # Conteo de notas 1
        if nota == 1:
            contador_unos += 1

    # Cálculo de promedios
    promedio_total = suma_total / 20

    promedio_mayor_5 = (
        suma_mayor_5 / contador_mayor_5
        if contador_mayor_5 > 0
        else 0
    )

    promedio_menor_4 = (
        suma_menor_4 / contador_menor_4
        if contador_menor_4 > 0
        else 0
    )

    # Resultados
    print("\nRESULTADOS:")
    print(f"Promedio total de notas: {promedio_total}")
    print(f"Promedio de notas mayores a 5: {promedio_mayor_5}")
    print(f"Promedio de notas menores a 4: {promedio_menor_4}")
    print(f"Cantidad de notas igual a 1: {contador_unos}")


if __name__ == "__main__":
    main()