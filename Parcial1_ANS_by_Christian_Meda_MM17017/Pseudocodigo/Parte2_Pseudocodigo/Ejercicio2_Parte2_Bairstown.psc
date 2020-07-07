Funcion val <- ab ( num )
	Si num<0 Entonces
		num=num*(-1)
	Fin Si
	val=num
Fin Funcion

Algoritmo Ejercicio2_Parte2_Bairstown
	Escribir "Raices de -9X^4+25X^3-5x^2-26x+24"
	a1=1
	a2=25/(-9)
	a3=-5/(-9)
	a4=-26/(-9)
	a5=24/(-9)
	r0=1.5
	s0=1.5
	r=0
	s=0
	deltaR=0
	deltaS=0
	Ear=1
	Eas=1
	errorEspecifico=0.05
	
	Escribir "I | R0 | S0 | B1 | B0 | C3 | C2 | C1 | DeltaR | DeltaS | S | R | Ear | Eas | x1 | x2"
	
	b4=0
	b3=0
	b2=0
	b1=0
	b0=0
	c4=0
	c3=0
	c2=0
	c1=0
	iterador=1
	
	Mientras Ear>errorEspecifico y Eas>errorEspecifico Hacer
		b4=a1
		b3=a2+b4*r0
		b2=a3+b3*r0+b4*s0
		b1=a4+b2*r0+b3*s0
		b0=a5+b1*r0+b2*s0
		
		c4=b4
		c3=b3+c4*r0
		c2=b2+c3*r0+c4*s0
		c1=b1+c2*r0+c3*s0
		
		deltaR=((-b1*c2)-(-b0*c3))/(c2*c2-c1*c3)
		deltaS=(c2*(-b0)-c1*(-b1))/(c2*c2-c1*c3)
		
		r=r0+deltaR
		s=r0+deltaS
		
		Ear=ab((deltaR/r)*100)
		Eas=ab((deltaS/s)*100)
		
		Escribir iterador," | ",r0," | ",s0," | ",b1," | ",b0," | ",c3," | ",c2," | ",c1," | ",deltaR," | ",deltaS," | ",r," | ",s," | ",Ear," | ",Eas," | continua | continua"
		r0=r
		s0=s

		iterador=iterador+1
	Fin Mientras
	
	
	x1=(r+rc((r^2)+4*s))/2
	x2=(r-rc((r^2)+4*s))/2
	
	Escribir x1
	Escribir x2
	
FinAlgoritmo
