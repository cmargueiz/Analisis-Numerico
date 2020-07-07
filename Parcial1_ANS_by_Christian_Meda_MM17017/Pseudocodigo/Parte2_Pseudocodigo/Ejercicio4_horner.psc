Funcion xi <- horner ( x0,r0,s0 )
	xi=x0-(r0/s0)
Fin Funcion
Funcion val <- ab ( num )
	Si num<0 Entonces
		num=num*(-1)
	Fin Si
	val=num
Fin Funcion
Algoritmo Ejercicio4_horner
	Escribir "Solucion para -x^3+2x^2+x-1"
	
	Escribir "Ingrese el valor inicial"
	Leer x0
	
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
	errorAproximado=ab((x0-hor)/hor)*100
	
	Escribir iterador," | ",hor," | ",errorAproximado
	
	
	Mientras errorAproximado>errorEspecifico Hacer
		x0=hor
		r3=a3
		r2=a2+r3*x0
		r1=a1+r2*x0
		r0=a0+r1*x0
		
		s2=r3
		s1=r2+s2*x0
		s0=r1+s1*x0
		hor=horner(x0,r0,s0)
		errorAproximado=ab((x0-hor)/hor)*100
		
		Escribir iterador," | ",hor," | ",errorAproximado
		iterador=iterador+1
	Fin Mientras
	
	Escribir "La raiz es: ",hor
	Escribir "Con error aproximado: ",errorAproximado
	
	
FinAlgoritmo
