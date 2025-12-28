
for number in range(10):
    if number == 5:
        break
    print(number)

print('=======Ejemplo==========')    

user = ['Andrea', 'Pedro', 'Anonimo', 'Marta', 'Diego']

for user in user:
    if user == 'Anonimo':
        print('Anonimo es Usuario Restringido')
        continue
    print(f'Bienvenido: {user}')


