// URI 1004 - Produto Simples
https://www.urionlinejudge.com.br/judge/pt/problems/view/1004 //

PROD = None
N2 = None
N1 = None

def read_integer():
  try:
    # read for Python 2.x
    return int(raw_input())
  except NameError:
    # read for Python 3.x
    return int(input())


N1 = read_integer()
N2 = read_integer()
PROD = N1 * N2
print(str("PROD = ") + str(PROD))