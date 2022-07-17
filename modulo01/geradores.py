from pympler.asizeof import asizesof

def dobro(lista):
  for i in lista:
    yield i * 2

def dobro2(lista):
  lista2 = []
  for i in lista:
    lista2.append(i*2)
  return lista2


print(asizesof(dobro2(range(100))))
print(asizesof(dobro(range(100))))