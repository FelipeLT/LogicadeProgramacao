//URI 1009 - Salário com Bônus
https://www.urionlinejudge.com.br/judge/pt/problems/view/1009 //

ttgrana2 = None
TTGRANA = None
SAL = None
COMISS = None
TTVEND = None
VEND = None

def read_string():
  try:
    # read for Python 2.x
    return raw_input()
  except NameError:
    # read for Python 3.x
    return input()

def read_numeric():
  try:
    # read for Python 2.x
    return float(raw_input())
  except NameError:
    # read for Python 3.x
    return float(input())


VEND = read_string()
SAL = read_numeric()
TTVEND = read_numeric()
COMISS = TTVEND * 0.15
TTGRANA = COMISS + SAL
ttgrana2 = "{:0.2f}".format(TTGRANA)
print(str("TOTAL = R$ ") + str(ttgrana2))
