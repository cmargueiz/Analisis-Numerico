Funcion r <- func ( x )
	r=sen(x)
Fin Funcion
Funcion f <- factorial ( x )
	acum=1
	Para i=1 Hasta x Con Paso 1 Hacer
		acum=acum*i
	Fin Para
	f=acum
Fin Funcion

Funcion e <- ErrorTeorico (xi)
	Dimension x(4)
	x(1)=0
	x(2)=pi/8
	x(3)=pi/4
	x(4)=pi/2
	
	e=(xi-x(1))*(xi-x(2))*(xi-x(3))*(cos(xi))/factorial(5)
Fin Funcion


Algoritmo Ejercicio1_newton_grado3
	Dimension xi(4)
	Dimension fx(4)
	Dimension DD[4,4]
	Dimension b(4)
	xi(1)=0
	xi(2)=pi/8
	xi(3)=pi/4
	xi(4)=pi/2
	
	fx(1)=func(0)
	fx(2)=func(pi/3)
	fx(3)=func(pi/4)
	fx(4)=func(pi/2)
	
	x=pi/16
	grado=3
	Para n<-1 Hasta grado Con Paso 1 Hacer
		DD[n,1]=fx(n)
	Fin Para
	
	Para k<-2 Hasta grado Con Paso 1 Hacer
		Para j<-k Hasta grado Con Paso 1 Hacer
			DD(j,k)=(DD(j,k-1)-DD(j-1,k-1))/(xi(j)-xi(j-k+1))
		Fin Para
		//Escribir ""
	Fin Para
	acum1=1
	acum2=0	
	Para a<-1 Hasta grado Con Paso 1 Hacer
		Para be<-1 Hasta a Con Paso 1 Hacer
			b(a)=DD[a,be]
			Escribir DD[a,be],", " Sin Saltar
		Fin Para
		Escribir ""
	Fin Para
	Para x<-1 Hasta grado Con Paso 1 Hacer
		Para ye<-1 Hasta grado Con Paso 1 Hacer
			acum1=acum1*(x-xi(ye))
		Fin Para
		acum2=acum2+(b(x)*acum1)
	Fin Para
	
	Escribir "Resultado: ",acum2
	Escribir "Error teorico: ",ErrorTeorico(pi/16)
FinAlgoritmo
