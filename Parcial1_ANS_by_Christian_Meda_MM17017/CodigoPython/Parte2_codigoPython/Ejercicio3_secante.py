from sympy import *

def f(x):
	return cos(x)-sin(x)+0.9

def secante(x1,x2):
	return x2-(f(x2)*(x1-x2)/(f(x1)-f(x2)))

def solucion(x1,x2):
		errorEspecifico=0.05
		errorAproximado=1

		if f(x1)*f(x2)<0:
			print "Existe raiz para f(X)=-sen(x)+cos(x)+0.9"
			itertador=1
			sec=0
			anterior=0
			actual=0
			sec=secante(x1,x2)
			print itertador," | ",x1," | ",x2," | ",f(x1)," | ",f(x2)," | ",sec," | -----------------"

			x1=x2
			x2=sec

			while errorAproximado>errorEspecifico:
				anterior=sec
				sec=secante(x1,x2)
				actual=sec
				x1=x2
				x2=sec
				errorAproximado=Abs((actual-anterior)/actual)*100
				print itertador," | ",x1," | ",x2," | ",f(x1)," | ",f(x2)," | ",sec," | ",errorAproximado
				itertador=itertador+1

			print "La raiz es: ",sec
			print "Con error ",errorAproximado
		else:
			print "No existe raiz en el rango ingresado"


print "Ingrese dos numero"

x1=float(input("valor 1\n"))
x2=float(input("valor 2\n"))

solucion(x1,x2)