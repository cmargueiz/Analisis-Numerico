Funcion r <- func ( x )
	r=(x^2)*cos(5*x+3)
Fin Funcion
Funcion f <- factorial ( x )
	acum=1
	Para i=1 Hasta x Con Paso 1 Hacer
		acum=acum*i
	Fin Para
	f=acum
Fin Funcion

Funcion e <- ErrorTeorico (xi)
	Dimension x(5)
	x(1)=0
	x(2)=pi/3
	x(3)=pi/4
	x(4)=pi/2
	x(5)=3*pi/4
	e=(xi-x(1))*(xi-x(2))*(xi-x(3))*(xi-x(4))*((2*cos(5*x(5)+3)-20*x(5)*sen(5*x(5)+3)-(25*x(5)^2)*cos(5*x(5)+3)))/factorial(2)
Fin Funcion


Algoritmo Ejercicio1_newton_grado1
	Dimension xi(5)
	Dimension fx(5)
	Dimension DD[5,5]
	Dimension b(5)
	xi(1)=0
	xi(2)=pi/3
	xi(3)=pi/4
	xi(4)=pi/2
	xi(5)=3*pi/4
	fx(1)=func(0)
	fx(2)=func(pi/3)
	fx(3)=func(pi/4)
	fx(4)=func(pi/2)
	fx(5)=func(3*pi/4)
	x=pi/8
	grado=1
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
	Escribir "Error teorico: ",ErrorTeorico(pi/8)
FinAlgoritmo
