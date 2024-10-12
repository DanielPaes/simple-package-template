from math import factorial

def resultado_combinacao(k, n):
        resultado = factorial(k) / (factorial(k - n)*(factorial(n)))
        return resultado