Funcion va <- ab (x )
	Si x<0 Entonces
		x=x*(-1)
	Fin Si
	va=x
Fin Funcion

Algoritmo baistown
	
	r0=1.5
	s0=1.5
	Ear=0
	Eas=0
	a4=1
	a3=-25/9
	a2=5/9
	a1=26/9
	a0=-24/9
	iterador=1
	errorEspecifico=0.05
	
	
	b4=a4
	b3=a3+b4*r0
	b2=a2+b3*r0+b4*s0
	b1=a1+b2*r0+b3*s0
	b0=a0+b1*r0+b2*s0
	
	c4=b4
	c3=b3+c4*r0
	c2=b2+c3*r0+c4*s0
	c1=b1+c2*r0+c3*s0
	Escribir c3
	deltaR=(-c3*b0+c2*b1)/(c1*c3-c2^2)
	deltaS=(-b1-(c2*deltaR))/c3
	
	r=r0+deltaR
	s=s0+deltaS
	
	Ear=ab(deltaR/r)*100
	Eas=ab(deltaS/s)*100
	
	Escribir iterador," | ",b1," | ",b0," | ",c3," | ",c2," | ",c1," | ",deltaR," | ",deltaS," | ",r," | ",s," | ",Ear," | ",Eas
	
	Mientras Ear>errorEspecifico || Eas>errorEspecifico Hacer
		r0=r
		s0=s
		b4=a4
		b3=a3+b4*r0
		b2=a2+b3*r0+b4*s0
		b1=a1+b2*r0+b3*s0
		b0=a0+b1*r0+b2*s0
		
		c4=b4
		c3=b3+c4*r0
		c2=b2+c3*r0+c4*s0
		c1=b1+c2*r0+c3*s0
		
		deltaR=(-c3*b0+c2*b1)/(c1*c3-c2^2)
		deltaS=(-b1-(c2*deltaR))/c3
		
		r=r0+deltaR
		s=s0+deltaS
		
		Ear=ab(deltaR/r)*100
		Eas=ab(deltaS/s)*100

		Escribir iterador," | ",b1," | ",b0," | ",c3," | ",c2," | ",c1," | ",deltaR," | ",deltaS," | ",r," | ",s," | ",Ear," | ",Eas
		iterador=iterador+1
	Fin Mientras
	
	x1=(r+rc((r^2)+4*s))/2
	x2=(r-rc((r^2)+4*s))/2
	
	//por division sintetica
	
	b4=a4
	b3=a3+b4*x1
	b2=a2+b3*x1
	b1=a1+b2*x1
	b0=a0+b1*x1
	Escribir b0
	
		c4=b4
		c3=b3+c4*x2
		c2=b2+c3*x2
		c1=b1+c2*x2
		d=(-1)*((c3^2)-4*c4*c2)
		x3=-c3/2
		x4=-c3/2
		
	
	Escribir x1
	Escribir x2
	Escribir x3,"+",d,"i/2"
	Escribir x4,"-",d,"i/2"
	
	
FinAlgoritmo
