
name = 'Andres Guzman'
curso = 'Curso Python'  
name_upper = name.upper()
print(name_upper)
print(name.upper())
print(curso.lower())

words = 'curso de python'
print(words.capitalize())
print(words.title())

words = '   Hola Mundo'
print(words.strip())
print(words.lstrip())
print(words.rstrip())

text = 'Hola Java'
print(text.replace('Java', 'Python'))

text = 'Andrez, Guzman, Python, Java'
data_list = text.split(',')
print(data_list[2])
print(data_list[3])

data = ['Andres2', 'Guzman2', 'Python2', 'Java2', 'Angula2']
text = ' '.join(data)
print(text)

text = 'Hola, Andres que tal como estas?'
print(text.find('Andres'))
print(text.index('tal'))
print(text.startswith('Andres'))
print(text.endswith('?'))

number = '1234'
decimal = '1234.45'
text = 'Python'
mix = 'Python3'

print(number.isalnum())
print(decimal.isdecimal())
print(mix.isalnum())
print(mix.isalpha())
print(text.isalpha())

text = '  Hola Andres, como estas? bienvenido al curso de Python'
tex_clean = text.strip().capitalize()
print(tex_clean)

new_text = tex_clean.replace('curso de Python', 'curso de Python 3')
print(new_text)



