from sympy import *
def g(x):
	return acos(sin(x)-0.9)

def dx(x):
	return -cos(x)/sqrt(1.8*sin(x)-(pow(sin(x),2))+0.19)

print "Para f(X)=-sen(x)+cos(x)+0.9"
print "G(x)=(cos(sen(x)+0.9))^1"
print "1. Determinar valor inicial"
print "2. Determinar rango"


op=int(input ("Ingrese la opcion"))
errorEspecifico=0.05
errorAproximado=1
gx=0

if op==1:
	r=float(input("Ingrese el valor inicial"))
	if dx(r) >1 :
		print "No hay convergencia"
		pass
elif op==2 :
	val1=float(input("Ingrese el primer valor"))
	val2=float(input("Ingrese el segundo valor"))
	if g(val1)>val1 and g(val2)<val2:
		print "valores: ",val1," y ",val2
		r=float(input("Ingrese el valor entre val1 y val2"))
		if (r>=val1 and r<=val2):
			r=r
		else:
			print "No existe ese valor en el rango"
	else:
		print "No hay convergencia"
else:
	print "Ha ingresado valores incorrectos"
	errorAproximado=0
	pass

if (dx(r))<1:
	iterador=1
		
	entrada=r

	while errorAproximado>errorEspecifico:
		salida=g(entrada)
			
		print iterador," | ",entrada," | ",salida," | ",errorAproximado
			
		errorAproximado=Abs((salida-entrada)/salida)*100
		entrada=salida
		iterador=iterador+1

	print "La raiz es: ",salida
	print "Con error: ",errorAproximado