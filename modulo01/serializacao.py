import pickle

lista = [1,2,3,4,5]

with open('arquivo.pkl', 'wb') as f:
  pickle.dump(lista, f)

with open('arquivo.pkl', 'rb') as arq:
  retornou = pickle.load(arq)
  print(retornou)