
Algoritmo Ejercicio2_Parte2_ferrari
	
	Escribir "Raices de -9X^4+25X^3-5x^2-26x+24"
	a=25/(-9)
	b=-5/(-9)
	c=-26/(-9)
	d=24/(-9)
	
	Escribir a
	Escribir b
	Escribir c
	Escribir d
	Escribir "-----------"
	
	P=(8*b-3*(a^2))/8
	Q=(8*c-4*a*b+a^3)/8
	R=(256*d-64*a*c+16*(a^2)*b-3*(a^4))/256
	Escribir P
	Escribir Q
	Escribir R
	Escribir "2-variables para formar la cubica"
	
	a2=-(P/2)
	b2=-(R)
	c2=((4*P*R)-(Q^2))/8
	Escribir a2
	Escribir b2
	Escribir c2
	Escribir "-----------------------"
	
	Escribir "3- Resolver por tartaglia"
	
	Escribir "-----------------------"
	
	p2=b2-(a2^2)/3
	q2=c2-((a2*b2)/3)+2*(a^3)/27
	
	Escribir p2 ," ",q2
	
	D=rc((4*(p2^3)+27*(q2^2))/108)
	Escribir D
	U=0
	Si D>0 Entonces
		A=-q2/2+rc((q2^2)/4+(q2^3)/27)
		B=-q2/2-rc((q2^2)/4+(q2^3)/27)
		U=(A^(1/3))+(B^(1/3))
		Escribir "D es mayor que 0"
		Escribir A
		Escribir B
		Escribir U
		U=U+(-a2/3)
	SiNo
		Si D<0 Entonces
			cosfi=(((27)^0.5)*q2)/((2*p2)*(-p2)^0.5)
			fi=acos(cosfi)
			U=(2*(-p/3)^0.5)*(cos(fi/3))
		SiNo
			Si D=0 Entonces
				U=2*((-q2/2)^(1/3))
			Fin Si
		Fin Si
	Fin Si
	
	Escribir "U=",U

	V=rc(2*U-P)
	W=Q/(-2*V)
	Escribir "V=",V
	Escribir "W=",W
	
	pcomp=(-1)*((V^2)-4*(U-W))
	x1=((V/2))-a/4
	x2=((V)/2)-a/4
	x3=-((V)/2)-a/4
	x4=-((V)/2)-a/4
	
	
	Escribir "Las raices son: "
	Escribir x1,"+",pcomp,"i/2"
	Escribir x2,"-",pcomp,"i/2"
	Escribir x3,"+",pcomp,"i/2"
	Escribir x4,"-",pcomp,"i/2"
FinAlgoritmo
