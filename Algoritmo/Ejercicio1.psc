Proceso Ejercicio1
	Definir iterador,ex Como Entero;
	Definir aproxActual,aproxAnterior,errorAprox,errorEspec,e,acumulador Como Real;
	iterador<-1;
	aproxActual<-1;
	aproxAnterior<-0;
	errorAprox<-1;
	errorEspec<-0.05;
	errorAprox<-1;
	acumulador<-1;
	Mientras errorAprox>errorEspec Hacer
		aproxAnterior<-acumulador;
		ex<-iterador-1;
		si ex==0 entonces
			acumulador<-1;
		SiNo
			acumulador<-acumulador+((-1)^(iterador-1))*((0.5)^(2*(iterador-1)));
		finsi
		aproxActual<-acumulador;
		Si iterador==1 Entonces
			Escribir iterador," ",aproxActual," ","----";
		SiNo
			errorAprox<-abs(((aproxActual-aproxAnterior)/aproxActual)*100);
			si errorAprox<0 entonces
				errorAprox<-errorAprox*(-1);
			FinSi
			Escribir iterador," ",aproxActual," ",errorAprox;
		FinSi
		iterador<-iterador+1;
	FinMientras
	
FinProceso
