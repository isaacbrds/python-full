numero1 = int(input('Digite o primeiro número: '))
numero2 = int(input('Digite o segundo número: '))
numero3 = int(input('Digite o terceiro número: '))

if numero1 >= numero2 and numero1 >= numero3:
  print('Numero1 é o maior dos tres numeros')
elif numero2 >= numero1 and numero2 >= numero3:
  print('Numero2 é o maior dos tres numeros')
else: 
  print('Numero3 é o maior dos tres numeros')