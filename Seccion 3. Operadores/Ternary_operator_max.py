
number1 = int(input('ingrese un numero: '))
number2 = int(input('ingrese un segundo numero: '))
number3 = int(input('ingrese un tercer numero: '))
number4 = int(input('ingrese un cuarto numero: '))

numbers = [number1, number2, number3, number4]

max = 0

for num in numbers:
    max = max if max > num else num

print(f'El numero mayor es {max}')

