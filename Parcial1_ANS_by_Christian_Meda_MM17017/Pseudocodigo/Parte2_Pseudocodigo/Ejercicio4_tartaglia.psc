Algoritmo Ejercicio4_tartaglia
	
	errorAproximado=1
	errorEspecifico=0.05
	
	
	a=-2
	b=-1
	c=1
	k=-a/3
	p=b-(a^2)/3
	q=c-((a*b)/3)+(2*(a^3)/27)
	
	
	

	D=(4*(p^3)+27*(q^2))/108
	
	
	Si D>0 Entonces
		Escribir "mayor"
		A=-q/2+rc((q^2)/4+(q^3)/27)
		B=-q/2-rc((q^2)/4+(q^3)/27)
		x1=(A^(1/3))+(B^(1/3))
		x2=-(((A)^(1/3))+((A)^(1/3)))/2+(3^(1/3))*(((A)^(1/3))-((A)^(1/3)))/2
		x3=-(((A)^(1/3))+((A)^(1/3)))/2-(3^(1/3))*(((A)^(1/3))-((A)^(1/3)))/2
		
		
	SiNo
		Si D<0 Entonces
			Escribir "p=",p
			Escribir "q=",q
			Escribir "menor"
			cosfi=((rc(27))*q)/((2*p)*rc(-p))
			Escribir "cosfi ",cosfi
			fi=acos(cosfi)
			Escribir "fi ",fi
			numpi= 3.14159265359
			x1=(2*rc(-p/3))*(cos(fi/3))+k
			x2=(2*rc(-p/3))*(cos(fi/3+(2*numpi/3)))+k
			x3=(2*rc(-p/3))*(cos(fi/3+(4*numpi/3)))+k
		SiNo
			Si D=0 Entonces
				Escribir "cero"
				x1=2*((-(q/2))^(1/3))+k
				x2=((q/2)^(1/3))+k
				x3=((q/2)^(1/3))+k
			Fin Si
		Fin Si
	Fin Si
	
	Escribir "Las raices son: "
	Escribir x1
	Escribir x2
	Escribir x3
FinAlgoritmo
