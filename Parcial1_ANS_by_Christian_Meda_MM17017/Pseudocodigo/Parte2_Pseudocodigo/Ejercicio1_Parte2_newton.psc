Funcion val	 <- derivada ( x )
	val=cos(x)-6
Fin Funcion
Funcion val <- f ( num )
	val=(sen(num)-6*num-5)
Fin Funcion
Funcion xi <- newton ( x )
	xi=x-(f(x)/derivada(x))
Fin Funcion

Funcion val <- ab ( num )
	Si num<0 Entonces
		num=num*(-1)
	Fin Si
	val=num
Fin Funcion

Algoritmo Ejercicio1_parte2_newton
	x=-2
	errorAproximado=1
	errorEspecifico=0.05
	iterador=1
	anterior=0
	actual=0	
	
	fx=f(x)
	fprima=derivada(x)
	xi=newton(x)
	errorAproximado=ab((x-xi)/xi)*100
	Escribir "iterador | f(xi) | dx(xi) | xi+1 | Ea"
	Escribir iterador," | ",fx," | ",fprima," | ",xi," | ",errorAproximado
	Mientras errorAproximado>errorEspecifico Hacer
		
		x=xi
		fx=f(x)
		fprima=derivada(x)
		xi=newton(x)
		errorAproximado=ab((x-xi)/xi)*100
		
		Escribir iterador," | ",fx," | ",fprima," | ",xi," | ",errorAproximado
		iterador=iterador+1
	Fin Mientras
	Escribir "El valor de la raiz es: ",xi
	Escribir "Con el error de: ",errorAproximado
	
FinAlgoritmo
