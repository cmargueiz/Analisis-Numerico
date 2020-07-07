from sympy import *
from math import *
from decimal import Decimal

def truncate(number):
    
    return trunc(number*100000)/100000;

x=pi/9
iterador=0
aproxActual=0
aproxAnterior=0
errorAprox=1
errorEspec=0.05
errorAprox=1
acumulador=0.0
actual=0
while (errorAprox>errorEspec) :
	aproxAnterior=acumulador
	acumulador=acumulador+(pow(x,(2*iterador+1)))/(factorial(2*iterador+1))
	aproxActual=acumulador
	
	if iterador==1:
		print(iterador,' ',aproxActual,' ','----')
	else:
		errorAprox=Abs(((aproxActual-aproxAnterior)/aproxActual)*100);

	iterador=iterador+1

print("Resultado: ",acumulador)
print("Valor al redondear hasta 4 decimales :",round(acumulador,4))
Er=Abs(acumulador-round(acumulador,4))
Err=Er/acumulador
Errp=Err*100
print "Er =",Er
print "Err =",Err
print "Errp =",Errp

print("Valor al truncar hasta 5 decimales :",round(acumulador))
Er=acumulador-truncate(acumulador)
Err=Er/acumulador
Errp=Err*100
print "Er =",Er
print "Err =",Err
print "Errp =",Errp
