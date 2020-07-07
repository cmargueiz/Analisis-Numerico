Proceso Ejercicio4
	Definir a,b,c,x1,x2 Como Real;
	a<-100;
	b<--10011;
	c<-10.011;
	
	Escribir "Forma1: Solucion de raices para",a,"x^2+",b,"+x+",c,"=0";
	
	x1<-(-b+((b^2)-4*a*c)^(1/2))/(2*a);
	x2<-(-b-((b^2)-4*a*c)^(1/2))/(2*a);
	
	Escribir x1;
	Escribir x2;
	
	Escribir "Forma2: Solucion de raices para: ",a,"x^2+",b,"+x+",c,"=0";
	
	x1<-(-2*c)/((b+((b^2)-4*a*c)^(1/2)));
	x2<-(-2*c)/((b-((b^2)-4*a*c)^(1/2)));
	
	Escribir x1;
	Escribir x2;
	
FinProceso
