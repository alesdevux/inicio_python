print('Vamos a mostrar una lista de números impares, entre los números que indiques')

numero_inicial = int(input('Ingrese un número inicial: '))
numero_final = int(input('Ingrese un número final: '))

if numero_inicial > numero_final:
  numero_inicial, numero_final = numero_final, numero_inicial

for num in range(numero_inicial, numero_final + 1):
  if num % 2 != 0:
    print(num)