def primo_o_no(num):
  if num == 1:
    return False
  elif num == 2:
    return True
  else:
    for i in range(2, num):
      if num % i == 0:
        return False
    return True
  
def inicio():
  print('Bienvenido a la calculadora de números primos o no primos')
  print('Ingrese un número entero a comprobar')
  num = int(input())
  if primo_o_no(num):
    print('El número', num, 'es primo')
  else:
    print('El número', num, 'no es primo')
    
inicio()