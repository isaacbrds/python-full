def soma_numeros(*args):
  soma = 0
  for i in args:
    soma += i
  print(soma)

soma_numeros(1,2,3,4,5,6,7,8,9,10)

def imprime_numeros(**kwargs):
  for i in kwargs.values():
    print(i)
    

imprime_numeros(num1 = 1, num2 = 2, num3 = 3, num4 = 4, num5 = 5)