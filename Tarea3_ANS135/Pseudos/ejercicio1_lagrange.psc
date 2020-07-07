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

Algoritmo Lagrange_ejercicio1_grado1
	Dimension xi(5)
	Dimension fx(5)
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
	n=1
	Escribir "Puntos: "
	Para i<-1 Hasta 5 Con Paso 1 Hacer
		Escribir xi(i)
	Fin Para
	Escribir "Interpolar para p(pi/8)"
	xint=pi/8
	fxint=0
	i=1;
	Mientras  i<=n+1 Hacer
    L=1;
    J=0;
    Mientras  J<=n hacer
	si i<>J+1 Entonces
		L=L*(xint-xi(J+1))/(xi(i)-xi(J+1));
	FinSi

    J=J+1;
Fin Mientras

	fxint=fxint+L*func(i);
	i=i+1;
FinMientras

	Escribir "Resultado Grado 1: ",fxint
	Escribir "Error teorico: ",ErrorTeorico(pi/8)
FinAlgoritmo
