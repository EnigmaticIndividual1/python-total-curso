
def main():
    nom1 = 'Raul'
    nom2 = 'Pablo'
    nom3 = 'Pedro'

    nuevo_nombre_1 = nom1[1].upper() + '.' + nom1[-2:]
    nuevo_nombre_2 = nom2[1].upper() + '.' + nom2[-2:]
    nuevo_nombre_3 = nom3[1].upper() + '.' + nom3[-2:]

    resultado = nuevo_nombre_1 + '_' + nuevo_nombre_2 + '_' + nuevo_nombre_3

    print(resultado)

if __name__ == '__main__':
    main()

