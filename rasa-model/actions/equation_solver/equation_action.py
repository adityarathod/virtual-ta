# work in progress
# i think you have to do `pip install antlr4-tools` outside the venv (but maybe try without it)
import process_latex
from sympy.solvers import solve

v = process_latex.process_sympy("\sum_{i = 1}^{10} i")
print(v)
print(type(v))
print(v.doit())

v = process_latex.process_sympy("x * 5 + 1 = 6")
print(v)
print(type(v))
print(solve(v))

v = process_latex.process_sympy("5 ^ 7")
print(v)
print(type(v))
print(v.doit())

v = process_latex.process_sympy("\int_{0}^{5} x")
print(v)
print(type(v))
print(v.doit())



# can't process this 
# v = process_latex.process_sympy("\lim_{n \to \infty}{1/x}")
# print(v)
# print(type(v))
# print(v.doit())