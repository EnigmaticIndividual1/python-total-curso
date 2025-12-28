def main():
    # VALIDACIÓN DEL NOMBRE
    while True:
        name = input('Introduce tu nombre: ')
        if name.replace(" ", "").isalpha():
            break
        else:
            print('ERROR: El nombre solo debe contener letras')

    print(f'Hola, {name}')

    # PRECIO
    price = int(input('Introduce el precio del producto en pesos: '))
    print(f'El valor final es {price} pesos')

    # PESO
    weight = float(input('Ingresa el peso del producto: '))
    print(f'El peso del producto es {weight} kilos')


if __name__ == "__main__":
    main()
