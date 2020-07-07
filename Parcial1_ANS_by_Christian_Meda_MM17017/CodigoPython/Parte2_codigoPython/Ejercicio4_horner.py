from sympy import *

def horner(x0,r0,s0):
	return x0-(r0/s0)

def solucion(x0):
	
	
	errorAproximado=1
	errorEspecifico=0.05
	
	a0=1
	a1=-1
	a2=-2
	a3=1
	r0=0
	r1=0
	r2=0
	r3=0
	s2=0
	s1=0
	s0=0
	iterador=1
	
	r3=a3
	r2=a2+r3*x0
	r1=a1+r2*x0
	r0=a0+r1*x0
	
	s2=r3
	s1=r2+s2*x0
	s0=r1+s1*x0
	hor=horner(x0,r0,s0)
	errorAproximado=Abs((x0-hor)/hor)*100

	while errorAproximado>errorEspecifico:
		x0=hor
		r3=a3
		r2=a2+r3*x0
		r1=a1+r2*x0
		r0=a0+r1*x0
		
		s2=r3
		s1=r2+s2*x0
		s0=r1+s1*x0
		hor=horner(x0,r0,s0)
		errorAproximado=Abs((x0-hor)/hor)*100
		
		print iterador," | ",hor," | ",errorAproximado
		iterador=iterador+1

	print "La raiz es: ",hor
	print "Con error aproximado: ",errorAproximado

print "Solucion para -x^3+2x^2+x-1"
	 
x0=float(input("Ingrese el valor inicial"))

solucion(x0)