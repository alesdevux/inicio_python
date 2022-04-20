def areaTriangular(base, altura):
  return (base * altura) / 2

def areaCirculo(radio):
  return 3.14 * radio ** 2

def calcularTriangulo():
  titulo = 'Vamos a calcular el área de un triángulo'
  print(titulo.upper())
  altura = float(input('Indique la altura del triangulo: ').replace(',', '.'))
  base = float(input('Indique la base del triangulo: ').replace(',', '.'))
  areaTriangular(base, altura)
  print('El área del triángulo es', areaTriangular(base, altura))
  
def calcularCirculo():
  titulo = 'Vamos a calcular el área de un círculo'
  print(titulo.upper())
  radio = float(input('Indique el radio del circulo: ').replace(',', '.'))
  areaCirculo(radio)
  print('El área del circulo es', areaCirculo(radio))

def inicio():
  print('Bienvenido a la calculadora de áreas')
  print('1. Calcular el área de un triángulo')
  print('2. Calcular el área de un círculo')
  print('3. Salir')
  opcion = int(input('Ingrese el número para seleccionar una opción: '))
  if opcion == 1:
    calcularTriangulo()
  if opcion == 2:
    calcularCirculo()
  if opcion == 3:
    print('Gracias por usar la calculadora de áreas')
  if opcion != 1 and opcion != 2 and opcion != 3:
    print('Opción inválida')
    inicio()
    
inicio()