print('=======While==========')
i = 0
while i <= 5:
    print(f'Contador es: {i}')
    i += 1

print('=======While List==========')
names = ['Andres', 'Pedro', 'Raul', 'Luis', 'Juan']
count = 0
while count < len(names):
    print(f'Nombre en posicion {count}: {names[count]}')
    count += 1

print('=======Do While==========')
i = 0
while True:
    print(i)
    i += 1
    if i >= 10:
        break

print('=======Do While Ejemplo==========')

correct_number = 7

while True:
    attempt = int(input('Adivina el numero del 1 al 10: '))
    if attempt == correct_number:
        print('Correcto! has adivinado el numero!')
        break
    else: 
        print('Numero incorrecto!, intenta de nuevo!')

    