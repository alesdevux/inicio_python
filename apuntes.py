# AND -> True, False
print('AND:')
print('t y t =', True and True)
print('t y f =', True and False)
print('f y t =', False and True)
print('f y f =', False and False)
print('\n')

# OR -> True, False
print('OR:')
print('t o t =', True or True)
print('t o f =', True or False)
print('f o t =', False or True)
print('f o f =', False or False)
print('\n')

# XOR -> True, False (Uno de los dos debe ser False para que sea True)
print('XOR:')
print('t x t =', True ^ True)
print('t x f =', True ^ False)
print('f x t =', False ^ True)
print('f x f =', False ^ False)
print('\n')

a = 5
b = 6
c = 7

resultado = (a >= 5 or c > 7)
# (True or False) = True
print('(a >= 5 or c > 7) =', resultado)

resultado = (a >= 5 and c > 7)
# (True and False) = False
print('(a >= 5 and c > 7) =', resultado)

resultado = ((a >= 5 or c > 7) and (b == 5))
# (True or False) and (False) = False
print('((a >= 5 or c > 7) and (b == 5)) =', resultado)

resultado = ((a >= 5 or c > 7) and (b == 5 or c == 7))
# (True or False) and (False or True) = True
print('((a >= 5 or c > 7) and (b == 5 or c == 7)) =', resultado)


# if condition:
  # do something
  # debemos usar siempre o espacios o tabulaciones
  # y siempre el mismo número de tabulaciones o espacios

if a == 5:
  print('a es igual a 5')
if a >= 5 and b <= 6:
  print('a es mayor o igual a 5 y b es menor o igual a 6')
  
if c == 7:
  print('c es igual a 7')
elif b == 6:
  print('b es igual a 6')

if b == 3:
  print('b es igual a 3')
elif b == 4:
  print('b es igual a 4')
else:
  print('b no es ni 3 ni 4')
  
contador = 0
while contador <= 10: # importante poner limite al while
  print('contador =', contador)
  contador += 1

fizzBuzz = 0
while fizzBuzz <= 15:
  if fizzBuzz % 3 == 0 and fizzBuzz % 5 == 0:
    print('FizzBuzz')
  elif fizzBuzz % 3 == 0:
    print('Fizz')
  elif fizzBuzz % 5 == 0:
    print('Buzz')
  else:
    print(fizzBuzz)
  fizzBuzz += 1

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
longitud = len(lista)
print('La lista tiene', longitud, 'items')
for valorActual in lista:
  print('valorActual =', valorActual)

listaPalabras = ['hola', 'mundo', 'python', 'es', 'un', 'lenguaje', 'de', 'programacion']
for palabra in listaPalabras:
  print('palabra =', palabra)
  if palabra == 'python':
    print('for: He encontrado en la lista', palabra)
    break

if 'python' in listaPalabras:
  print('if: He encontrado en la lista el mejor lenguaje de programación, que es python')
  
listaL = ['a', 'A', 'p', 'P', 'Z', 'z']
listaLOrdenada = sorted(listaL) 
# sorted() devuelve una lista ordenada
# por defecto, ordena usando el codigo ASCII
# se le puede pasar una función para ordenar
# por ejemplo, ordenar por orden alfabético con sorted(listaL, key=str.lower)
print('listaL =', listaL)
print('listaLOrdenada =', listaLOrdenada)

for letra in listaL:
  pass 
  # debemos usar pass para que no de error
  # ya que sí o sí debemos hacer que haga algo al iterar
  
if 'a' in listaL:
  pass
  # o en general, cuando debemos escribir algo en identaciones
  # debemos usar pass si no ejecutamos todavía nada