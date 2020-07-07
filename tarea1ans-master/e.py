from sympy import *

def calculo(CS, X):
    if CS != "" and X !="":
        cifras = int(CS)
        var = float(X)
        Ea = 0
        iteracion = 0
        anterior = 0

        Es = (0.5*pow(10, (2-cifras)))

        actual = pow(var, iteracion)/factorial(iteracion)
        Ea = float(((actual - anterior)/actual)*100)
        iteracion = iteracion+1

        valores = [[iteracion,actual,"---"]]
        while (Abs(Ea) > Es):

            anterior = actual
            actual = anterior + (pow(var, iteracion)/factorial(iteracion))
            Ea = float(((actual - anterior)/actual)*100)
            iteracion = iteracion+1
            
            lista = [iteracion, actual, Abs(Ea)]
            valores.append(lista)
        return valores