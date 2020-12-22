// URI - 1003 - Soma Simples 
https://www.urionlinejudge.com.br/judge/pt/problems/view/1003 //

A = None
B = None
X = None

def read_integer():
  try:
    # read for Python 2.x
    return int(raw_input())
  except NameError:
    # read for Python 3.x
    return int(input())


A = read_integer()
B = read_integer()
X = A + B
print(str("SOMA = ") + str(X))
