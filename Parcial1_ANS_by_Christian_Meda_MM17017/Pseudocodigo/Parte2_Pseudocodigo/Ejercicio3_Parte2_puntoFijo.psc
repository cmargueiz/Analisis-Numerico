Funcion val <- g ( x )
	val=acos(sen(x)-0.9)
Fin Funcion

Funcion val <- dx ( x )
	val=-cos(x)/rc(1.8*sen(x)-((sen(x))^2)+0.19)
Fin Funcion

Funcion val <- ab ( num )
	Si num<0 Entonces
		num=num*(-1)
	Fin Si
	val=num
Fin Funcion

Algoritmo Ejercicio4_puntofijo
	Escribir "Para f(X)=-sen(x)+cos(x)+0.9"
	Escribir "G(x)=(cos(sen(x)+0.9))^1"
	Escribir "1. Determinar valor inicial"
	Escribir "2. Determinar rango"
	Escribir "Ingrese opcion"
	Leer op
	
	errorEspecifico=0.05
	errorAproximado=1
	gx=0
	
	Segun op Hacer
		1:
			Escribir "Ingrese valor inicial"
			Leer r
			Si dx(r) >1 Entonces
				Escribir "No hay convergencia"
			FinSi
			
		2:
			Escribir "Ingrese el primer valor"
			leer val1
			Escribir "ingrese el segundo valor"
			leer val2
			Si g(val1)>val1 y g(val2)<val2 Entonces
				Escribir "ingrese un valor entre",val1," y ",val2
				leer r
				Si r>=val1 y r<=val2 Entonces
					r=r
				SiNo
					Escribir "No existe ese valor en el rango adecuado"
				Fin Si
			SiNo
				Escribir "No existe convergencia"
			Fin Si

		De Otro Modo:
			Escribir "Ha ingresado valores incorrectos"
			errorAproximado=0
	Fin Segun
	

	Si dx(r) <1 Entonces
		iterador=1
		
		entrada=r
		
		Mientras errorAproximado>errorEspecifico Hacer
			
			salida=g(entrada)
			
			Escribir iterador," | ",entrada," | ",salida," | ",errorAproximado
			
			errorAproximado=ab((salida-entrada)/salida)*100
			entrada=salida
			iterador=iterador+1
		Fin Mientras
		Escribir "La raiz es: ",salida
		Escribir "Con error: ",errorAproximado
	Fin Si
	
		
FinAlgoritmo
