def soma(n1,n2):
  if n1<0 or n2<0:
    raise ValueError('N1 e N2 não podem ser negativos')
  return n1 + n2

soma(1,-1)