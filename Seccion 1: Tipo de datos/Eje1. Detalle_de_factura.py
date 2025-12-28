
def main():
    nombre_factura = "Productos oficina"

    precio_producto_1 = 54.99
    precio_producto_2 = 79.79

    total_bruto = precio_producto_1 + precio_producto_2
    impuesto = total_bruto * 0.19
    total_neto = total_bruto + impuesto

    print(
        f'La factura {nombre_factura} tiene un total de {total_bruto} dolares, ' 
        f'con un impuesto de {impuesto} y el monto total mas impuestos es {total_neto} dolares.')

if __name__ == '__main__':
        main()
