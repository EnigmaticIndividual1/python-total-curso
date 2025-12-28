
name = 'Andres'
age = 40
text = f'Hola, me {name} y tengo {age} años'
print(text)

a = 5
b = 3
print(f'la suma de {a} y {b} es {a+b}')

result = f'El precio del articulo es de {a * b} pesos'
print(result)

price = 49
txt = f'Esta producto es muy { 'caro' if price >= 50 else 'barato'}'
print(txt)

fruit = 'Manzanas'
txt = f'Me encantan las {fruit.capitalize()}'
print(txt)
