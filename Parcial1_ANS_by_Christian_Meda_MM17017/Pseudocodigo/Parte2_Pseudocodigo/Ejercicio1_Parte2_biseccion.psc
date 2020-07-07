Funcion val <- ab (num)
	Si num<0 Entonces
		num <- num*(-1)
	FinSi
	val <- num
FinFuncion

Funcion val <- f (num)
	val <- (sen(num)-6*num-5)
FinFuncion

Algoritmo Ejercicio1_parte1_biseccion
	// Evaluando valores
	x1 <- -2
	x2 <- -0.9
	errorAproximado <- 1
	errorEspecifico <- 0.05
	iterador <- 1
	condicion <- ''
	anterior <- 0
	actual <- 0
	Si (f(x1)*f(x2))<0 Entonces
		Escribir 'valores validos'
		Escribir 'i | x1 | x2 | xr | fx1 | fx2 | fxr | fx1*fxr | condicion | EA'
		xr <- (x1+x2)/2
		Si f(x1)*f(xr)<0 Entonces
			condicion <- '<'
		SiNo
			Si f(x1)*f(xr)>0 Entonces
				condicion <- '>'
			FinSi
		FinSi
		Escribir iterador,' | ',x1,' | ',x2,' | ',xr,' | ',f(x1),' | ',f(x2),' | ',f(xr),' | ',fx1*fxr,' | ',condicion,' | ',errorAproximado
		Si f(x1)*f(xr)<0 Entonces
			x2 <- xr
			condicion <- '<'
		SiNo
			Si f(x1)*f(xr)>0 Entonces
				x1 <- xr
				condicion <- '>'
			SiNo
				Si f(x1)*f(xr)==0 Entonces
					Escribir 'La raiz es: ',xr
				FinSi
			FinSi
		FinSi
		Si f(x1)*f(xr)!=0 Entonces
			Mientras errorAproximado>errorEspecifico Hacer
				anterior <- xr
				xr <- (x1+x2)/2
				actual <- xr
				fx1 <- f(x1)
				fx2 <- f(x2)
				fxr <- f(xr)
				Si f(x1)*f(xr)<0 Entonces
					x2 <- xr
					condicion <- '<'
				SiNo
					Si f(x1)*f(xr)>0 Entonces
						x1 <- xr
						condicion <- '>'
					SiNo
						Si f(x1)*f(xr)==0 Entonces
							Escribir 'La raiz es: ',xr
							errorAproximado <- 0
						FinSi
					FinSi
				FinSi
				Si iterador!=1 Entonces
					errorAproximado <- ab((anterior-actual)/actual)*100
				FinSi
				Escribir iterador,' | ',x1,' | ',x2,' | ',xr,' | ',fx1,' | ',fx2,' | ',fxr,' | ',fx1*fxr,' | ',condicion,' | ',errorAproximado
				iterador <- iterador+1
			FinMientras
		FinSi
	SiNo
		Escribir 'Valores invalidos'
	FinSi
	Escribir 'Resultado=',xr
	Escribir "Error aproximado= ",errorAproximado
FinAlgoritmo
