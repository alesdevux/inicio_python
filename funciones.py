def miFuncion(nombre):
  print('Hola', nombre)


def matematicas(num1, num2):
  def suma(a, b):
    print(a, '+', b, '=', a + b)
    
  def resta(a, b):
    print(a, '-', b, '=', a - b)
    
  def multiplicacion(a, b):
    print(a, '*', b, '=', a * b)
    
  def division(a, b):
    print(a, '/', b, '=', a / b)
    
  def residuo(a, b):
    print(a, '%', b, '=', a % b)
    
  suma(num1, num2)
  resta(num1, num2)
  multiplicacion(num1, num2)
  division(num1, num2)
  residuo(num1, num2)
  # al igual que las variables, al crearse dentro de una función,
  # solo pueden ser usadas dentro de la función

miFuncion('Juan')
miFuncion('Pedro')
matematicas(5, 6)

temperaturaHoy = 20.3

def tiempo(nombre = 'Ales'):
  global temperaturaHoy
  temperaturaHoy = 12.6
  # dentro la función, la variable temperaturaHoy es diferente a la que
  # está fuera de la función, se crea una nueva variable local
  # para cambiar el valor de la variable global temperaturaHoy
  # se debe usar la palabra reservada global
  # así usamos la variable global
  print('Hola', nombre)
  print('La temperatura hoy es', temperaturaHoy)

tiempo('Juan')
tiempo()
print('La temperatura hoy es', temperaturaHoy, 'fuera de la función')

# los parametros opcionales deben ir al final o ser todos opcionales
# def suma(a, b = 0, c): # error, b deberia ir al final o c ser opcional
def resta(a = 0, b = 0, c = 0):
  print(a, '-', b, '-', c, '=', a - b - c)

resta(1)
resta(1, 3)
resta(1, 3, 5)
# podemos asignar un parametro concreto a un parametro opcional
resta(b = 3)

# podemos pasar una lista de parametros a una función
# sin saber cuantos parametros se pasan, podemos usar *args
def suma(*args):
  total = 0
  for num in args:
    total += num
  print('La suma de los numeros es', total)
  
suma(1, 2, 3, 4, 5)
suma(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# también se puede pasar **kwargs
# para pasar un diccionario de parametros a una función
def sumaDiccionario(**kwargs):
  total = 0
  for num in kwargs.values():
    total += num
  print('La suma de los numeros del diccionario es', total)
  
def diccionario(**kwargs):
  print(kwargs)
  for key, value in kwargs.items():
    print(key, '=', value)
  # no podemos usar una clave que no exista en el diccionario
  # es decir que no le estemos pasando
  # if kwargs['nombre'] == 'Juan': # (error)
  if 'nombre' in kwargs.keys():
    print('El nombre es', kwargs['nombre'])
      

sumaDiccionario(a = 1, b = 2, c = 3)
diccionario(nombre = 'Juan', apellido = 'Perez', edad = 30)
diccionario(apellido = 'Perez', edad = 30, otro = 'otro')

# las funciones por lo general no hacen print,
# sino que devuelven un valor, usando return

def operaciones (a, b):
  return a + b, a - b, a * b, a / b, a % b

resultado = operaciones(1, 2)
print(resultado)
# si hacemos más de un return, devuelve una tupla
# así podemos acceder a los valores de la tupla con un indice
print(resultado[0])
print(resultado[1])

# también podemos asignar una variable a cada valor del return (tupla)
# eso sí, es obligatorio crear una variable para cada valor
suma, resta, multiplicacion, division, residuo = operaciones(6, 2)
print('El resultado de la suma es', suma)
print('El resultado de la resta es', resta)
print('El resultado de la multiplicacion es', multiplicacion)
print('El resultado de la division es', division)
print('El resultado de la división entera es', residuo)


def sumador(**kwargs):
  inicial = kwargs['inicial'] if 'inicial' in kwargs else 0
  final = kwargs['final'] if 'final' in kwargs else inicial
  # podemos usar el operador ternario para asignar un valor a una variable
  
  resultado = 0
  for num in range(inicial, final + 1):
    resultado += num
  return resultado

resSumador = sumador(inicial = 6, final = 10)
print('El resultado del sumador es', resSumador)

# FUNCIONES ANONIMAS
# se usa la palabra reservada lambda para crear una función anónima
# podemos pasarles parametros, pero no entre ()
# no se puede usar return, ya lo hace por sí mismo
anonima = lambda nombre, apellido: print('Hola', nombre, apellido)
anonima('Rocio', 'Perez')

sumatoria = lambda *args: sum(args)
print(sumatoria(1, 2, 3, 4, 5))