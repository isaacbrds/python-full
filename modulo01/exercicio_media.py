nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))
nota3 = float(input('Digite sua terceira nota: '))
nota4 = float(input('Digite sua quarta nota: '))


media = (nota1 + nota2 + nota3 + nota4)/4

if media >= 7:
  print(f'Parabens você foi aprovado com média {media}!!!')
elif media >= 4:
  print(f'Você não foi aprovado está com média {media}, mas poderá fazer a recuperação ')
else:
  print(f'Infelizmente você foi reprovado com média {media}!!!')

