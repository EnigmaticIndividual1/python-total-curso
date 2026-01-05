usernames = ['andres', 'admin', 'pepe', 'jandresosefa']
passwords = ['1234', '12345', '123', 'abcde']

user = input('Ingresa tu username: ')
password = input('Ingresa tu password: ')

authenticated = False

for i in range(len(usernames)):
    print(i)
    if usernames[i] == user and passwords[i] == password:
        authenticated = True
        break

if authenticated:
    print(f'Bienvenido usuario {user}, ha iniciado sesion con exito!')
else: 
    print('Username o Password incorrecto! \nLo sentimos, requieres autenticacion!')

