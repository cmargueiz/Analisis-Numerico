Proceso Ejericio5
	Definir iterador,ex,i Como Entero;
	Definir aproxActual,aproxAnterior,errorAprox,errorEspec,factorial,acumulador Como Real;
	iterador<-1;
	aproxActual<-1;
	aproxAnterior<-0;
	errorAprox<-1;
	factorial<-1;
	errorEspec<-(0.5*10^(2-20));
	errorAprox<-1;
	acumulador<-1;
	
	Escribir "****************Primera serie Taylor***************";
	
	Mientras errorAprox>errorEspec Hacer
		aproxAnterior<-acumulador;
		ex<-iterador-1;
		si ex==0 entonces
			acumulador<-1;
		SiNo
			
			Para i<-1 Hasta ex Con Paso 1 Hacer
				factorial<-factorial*i;
			FinPara
			acumulador<-acumulador +(((-5)^(ex))/ (factorial));
			factorial<-1;
			
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
