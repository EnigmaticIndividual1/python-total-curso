usernames = ['andres', 'admin', 'pepe', 'jandresosefa']
passwords = ['1234', '12345', '123', 'abcde']

user = input('Ingresa tu username: ')
password = input('Ingresa tu password: ')

authenticated = False

for i in range(len(usernames)):
    # print(i)
    authenticated = True if usernames[i] == user and passwords[i] == password else False
    if authenticated:
        break 
    # if usernames[i] == user and passwords[i] == password:
    #     authenticated = True
    #     break
message = f'Bienvenido Usuario {user}, ha iniciado sesion con exito' \
    if authenticated else 'Username o password incorrecto \nLo sentimos, requiere autenticacion'
print(f'message = {message}')
# if authenticated:
#     print(f'Bienvenido usuario {user}, ha iniciado sesion con exito!')
# else: 
#     print('Username o Password incorrecto! \nLo sentimos, requieres autenticacion!')

