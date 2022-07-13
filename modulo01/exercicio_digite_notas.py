nota = int(input('Digite a nota do aluno:  '))

while nota < 0 or nota > 10:
  nota = int(input('Digite a nota do aluno:  '))

print(f'A nota digitada foi: {nota}')