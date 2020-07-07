from sympy import *

def f(num):
	return float(sin(num)-6*num-5)

def dx(num):
	return float(cos(num)-6)	

def dxx(num):
	return float(-sin(num))	

def newton(x):
    return float(x-(f(x)/dx(x)))

def solucionByNewton(x):
	convergencia=(f(x)*dxx(x))/pow(dx(x),2)

	if convergencia<1:
		errorAproximado=1
		errorEspecifico=0.05
		iterador=1
		anterior=0
		actual=0	
	
		fx=f(x)
		fprima=dx(x)
		xi=newton(x)
		errorAproximado=Abs((x-xi)/xi)*100
		print "iterador | f(xi) | dx(xi) | xi+1 | Ea"
		print iterador," | ",fx," | ",fprima," | ",xi," | ",errorAproximado

		while errorAproximado>errorEspecifico:
			x=xi
			fx=f(x)
			fprima=dx(x)
			xi=newton(x)
			errorAproximado=Abs((x-xi)/xi)*100
			print iterador," | ",fx," | ",fprima," | ",xi," | ",errorAproximado
			iterador=iterador+1	
	print "El valor de la raiz es: ",xi
	print "Con el error de: ",errorAproximado

solucionByNewton(-2)