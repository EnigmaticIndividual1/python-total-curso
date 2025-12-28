def main():
    num1 = int(input("Ingrese el primer número entero: "))
    num2 = int(input("Ingrese el segundo número entero: "))

    # Determinar el signo del resultado
    negativo = False
    if (num1 < 0 and num2 > 0) or (num1 > 0 and num2 < 0):
        negativo = True

    # Trabajar con valores absolutos
    a = abs(num1)
    b = abs(num2)

    resultado = 0

    # Multiplicación por suma repetida
    for _ in range(a):
        resultado += b

    # Aplicar signo
    if negativo:
        resultado = -resultado

    print(f"El resultado de la multiplicación es: {resultado}")


if __name__ == "__main__":
    main()