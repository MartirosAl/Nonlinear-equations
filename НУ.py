import sympy as sp
import scipy as scp
import math

x = sp.symbols('x')
l = sp.symbols('l')

def input_function():
    expr_str = input("Введите функцию: ")
    expr = sp.parse_expr(expr_str, local_dict={'x': x})
    return lambda x_val: expr.subs(x, x_val).evalf(), expr_str

def derivative(func):
    return lambda x_val: sp.simplify(sp.diff(func, x)).subs(x, x_val).evalf(), sp.diff(func, x)

def main_condition(a, b, func, d_func):
    if not(func(a) < 0 and func(b) > 0):
        return -1
    if d_func(a) < 0 and d_func(b) < 0:
        return -2
    if d_func(a) > 0 and d_func(b) > 0:
        return 0
    if d_func(a) == 0:
        return 1
    if d_func(b) == 0:
        return 2


a = int(input("Введите нижнюю границу: "))
b = int(input("Введите верхнюю границу: "))
while (a >= b):
    print("Неправильная граница")
    a = int(input("Введите нижнюю границу: "))
    b = int(input("Введите верхнюю границу: "))

func, func_str = input_function()
d_func, d_func_str = derivative(func_str)
mc = main_condition(a, b, func, d_func)

if (mc == -2):
    func = lambda x: -func(x);
elif (mc == -1):
    print ("Wrong function")
elif (mc == 1):
    a += 0.01
elif (mc == 2):
    b -= 0.01

k1 = max(d_func(a), d_func(b))
k2 = min(d_func(a), d_func(b))

fi = lambda x, l: x - l * func(x)
d_fi = lambda x, l: 1 - l * d_func(x)

print("Введите решение: |(", d_func_str ,")\'| = 0, если слева полож, а справа отриц")
max = int(input())
lam = round(abs(2/max), 2) - 0.01
if (abs(1 - lam*k2) < abs(1 - lam*k1)):
    alfa = abs(1 - lam*k1)
else:
    alfa = abs(1 - lam*k2)

x0 = (a + b) / 2
x1 = fi(x0, lam)
eps = 10**-2
n = math.ceil(math.log(eps/(abs(x0-x1)) * (1 - alfa), alfa))
xn = x1
print ("x0 = ", x0)
print ("x1 = ", x1)
for i in range(n-1):
    print("x",i + 2,"=", fi(xn, lam))

print(alfa, n, abs(x0-x1))
print(a, b)
print(k1, k2)
print(lam)