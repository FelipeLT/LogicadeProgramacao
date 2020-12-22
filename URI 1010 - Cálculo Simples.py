// URI 1010 - Cálculo Simples
https://www.urionlinejudge.com.br/judge/pt/problems/view/1010 //

ttfinal = None
ttfatura = None
faturapc2 = None
faturapc1 = None
valpc2 = None
epc2 = None
valpc1 = None
epc1 = None
peca2 = None
cod2 = None
peca1 = None
cod1 = None

def read_line():
  try:
    # read for Python 2.x
    return raw_input()
  except NameError:
    # read for Python 3.x
    return input()


peca1 = read_line().split(" ")
cod1 = int((peca1.pop(0)))
epc1 = int((peca1[0]))
valpc1 = float((peca1[-1]))
peca2 = read_line().split(" ")
cod2 = int((peca2.pop(0)))
epc2 = int((peca2[0]))
valpc2 = float((peca2[-1]))
faturapc1 = epc1 * valpc1
faturapc2 = epc2 * valpc2
ttfatura = float((faturapc1 + faturapc2))
ttfinal = "{:0.2f}".format(ttfatura)
print(str("VALOR A PAGAR: R$ ") + str(ttfinal))