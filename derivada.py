from sympy import*
from scipy.misc import derivative
import math
init_printing(use_unicode=True)

print('DERIVADA')

func = []
x = Symbol('x')
y = eval(input('DIGITE AQUI A SUA FUNÇÃO: '))
deri = y.diff(x)
func.append(str(deri))

n = int(input('DIGITE AQUI QUANTAS DERIVADAS DESEJA FAZER: '))

for i in range(n):
    deri = deri.diff(x)
    func.append(str(deri))

s1 = []
print('As derivadas da função são: ',y)
for i in range(n):
    s = eval(func[i])
    s1.append(s)
    print('Derivada d^('+str(i+1)+')/dx^('+str(i+1)+') = ',s)

y1 = (input('DIGITE AQUI A SUA FUNÇÃO DERIVADA: '))
x = eval(input('DIGITE AQUI O VALOR PARA x: '))
def f(x):
    y2 = eval(y1)
    return y2
print('O valor da derivada = {:.4f} '.format(f(x)))