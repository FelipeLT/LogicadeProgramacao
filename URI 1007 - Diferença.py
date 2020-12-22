// URI 1007 - Diferença
https://www.urionlinejudge.com.br/judge/pt/problems/view/1007 //

A = None
B = None
C = None
D = None
DIF = None
PRODAB = None
PRODCD = None

def read_integer():
  try:
    # read for Python 2.x
    return int(raw_input())
  except NameError:
    # read for Python 3.x
    return int(input())


A = read_integer()
B = read_integer()
C = read_integer()
D = read_integer()
PRODAB = A * B
PRODCD = C * D
DIF = PRODAB - PRODCD
print(str("DIFERENCA = ") + str(DIF))