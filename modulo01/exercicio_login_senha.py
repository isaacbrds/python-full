usuario = 'isaac'
senha = '123'

while True:
  if usuario == usuario_digitado and senha_digitado == senha:
    print('Usuário e senha corretos!!!')
    break
  print('Usuário ou senha errados!!!')
  usuario_digitado = input('Digite seu nome de usuário: ')
  senha_digitado = input('Digite sua senha: ')