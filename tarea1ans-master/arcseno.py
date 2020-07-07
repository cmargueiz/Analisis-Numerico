from sympy import *

def calculo(CS, X):
    if CS != "" and X !="":
        cifras = int(CS)
        var = float(X)
        Ea = 0
        iteracion = 0
        anterior = 0

        Es = (0.5*pow(10, (2-cifras)))
        
        p = (2*iteracion)+1
        actual = (factorial(2*iteracion)/pow(pow(2, iteracion)*factorial(iteracion) ,2))*(pow(var, p)/(p))
        Ea = float(((actual - anterior)/actual)*100)
        iteracion = iteracion+1
        
        valores = [[iteracion,actual,"---"]]
        while (Abs(Ea) > Es):
            p = (2*iteracion)+1
            anterior = actual
            actual = anterior + (factorial(2*iteracion) / pow((pow(2, iteracion)*factorial(iteracion)) ,2))*(pow(var, p)/(p))
            Ea = float(((actual - anterior)/actual)*100)
            iteracion = iteracion+1
            lista = [iteracion, actual, Abs(Ea)]
            valores.append(lista)
        return valores