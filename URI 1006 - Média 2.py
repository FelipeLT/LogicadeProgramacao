// URI - 1006 - Média 2
https://www.urionlinejudge.com.br/judge/pt/problems/view/1006 //

A = None
B = None
C = None
MED = None
MED2 = None
PESO_A = None
PESO_B = None
PESO_C = None

def read_numeric():
  try:
    # read for Python 2.x
    return float(raw_input())
  except NameError:
    # read for Python 3.x
    return float(input())


A = read_numeric()
B = read_numeric()
C = read_numeric()
PESO_A = A * 2
PESO_B = B * 3
PESO_C = C * 5
MED = PESO_A + (PESO_B + PESO_C)
MED2 = MED / 10
MED2 = "{:0.1f}".format(MED2)
print(str("MEDIA = ") + str(MED2))