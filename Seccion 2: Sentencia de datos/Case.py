
number = 2

match number:
    case 1:
        print('Seleccionaste la opcion 1')
    case 2: 
        print('Seleccionaste la opcion 2')
    case 3: 
        print('Seleccionaste la opcion 3')
    case 4:
        print('Opcion no valida')
     
def option(number):
    response = None
    if number == 1:
        response 'Seleccionaste la opcion 1'
    elif number == 2: 
        response'Seleccionaste la opcion 2'
    elif number == 3: 
        response'Seleccionaste la opcion 3'
    else: 
        response 'Opcion no valida'
result = option(3)
print(result)

name = input('Ingresa el nombre de la persona: ')

match name: 
    case 'Pepe':
        print('Hola Pepe!')
    case 'Juan':
        print('Hola Juan')
    case 'Maria':
        print('Hola Maria')
    case _:
        print('Hola Invitado') 
          