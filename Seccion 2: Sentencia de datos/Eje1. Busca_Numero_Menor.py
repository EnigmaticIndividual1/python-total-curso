def main():
    # Pedir cantidad de números (mínimo 10)
    cantidad = int(input("¿Cuántos números deseas comparar? (mínimo 10): "))

    if cantidad < 10:
        print("ERROR: Debes ingresar al menos 10 números.")
        return

    # Pedir el primer número para inicializar el menor
    menor = int(input("Ingresa el número 1: "))

    # Iterar para pedir el resto de los números
    for i in range(2, cantidad + 1):
        numero = int(input(f"Ingresa el número {i}: "))
        if numero < menor:
            menor = numero

    # Mostrar resultado
    print(f"\nEl número menor es: {menor}")

    if menor < 10:
        print("El número menor es menor que 10!")
    else:
        print("El número menor es igual o mayor que 10!")


if __name__ == "__main__":
    main()
