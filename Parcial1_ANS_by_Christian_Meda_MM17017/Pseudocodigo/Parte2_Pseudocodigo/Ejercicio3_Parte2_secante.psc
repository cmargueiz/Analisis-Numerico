Funcion val <- f ( x )
	val=cos(x)-sen(x)+0.9
Fin Funcion

Funcion val <- secante ( x1,x2 )
	val=x2-(f(x2)*(x1-x2)/(f(x1)-f(x2)))
Fin Funcion
Funcion val <- ab ( num )
	Si num<0 Entonces
		num=num*(-1)
	Fin Si
	val=num
Fin Funcion

Algoritmo Ejercicio3_secante
	
	errorEspecifico=0.05
	errorAproximado=1
	
	Escribir "Ingrese el primer valor"
	leer x1
	Escribir "Ingrese el segundo valor"
	Leer x2
	Si f(x1)*f(x2)<0 Entonces
		Escribir "Existe raiz para f(X)=-sen(x)+cos(x)+0.9"
		itertador=1
		sec=0
		anterior=0
		actual=0
		sec=secante(x1,x2)
		Escribir itertador," | ",x1," | ",x2," | ",f(x1)," | ",f(x2)," | ",sec," | -----------------"
		
		x1=x2
		x2=sec
		
		Mientras errorAproximado>errorEspecifico Hacer
			anterior=sec
			sec=secante(x1,x2)
			actual=sec
			x1=x2
			x2=sec
			errorAproximado=ab((actual-anterior)/actual)*100
			Escribir itertador," | ",x1," | ",x2," | ",f(x1)," | ",f(x2)," | ",sec," | ",errorAproximado
			itertador=itertador+1
		Fin Mientras
		
		Escribir "La raiz es: ",sec
		Escribir "Con error ",errorAproximado
	SiNo
		Escribir "No existe raiz"
	Fin Si
	
	
	
FinAlgoritmo
