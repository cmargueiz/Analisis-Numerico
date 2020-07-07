Funcion fact <- factorial ( num )
	acumulador=1
	Para i<-1 Hasta num Con Paso 1 Hacer
		acumulador=acumulador*i
	Fin Para
	fact=acumulador
Fin Funcion
Funcion calculo <- redondear ( val )
	calculo=Redon(val*10000)/10000;
Fin Funcion
Funcion calculo <- truncar ( val)
	calculo=TRUNC(val*100000)/100000;
Fin Funcion


Algoritmo Ejercicio5_parte1
	x=3.14159265358979323846/9
	iterador=0;
	aproxActual=0;
	aproxAnterior=0;
	errorAprox=1;
	errorEspec=0.05;
	errorAprox=1;
	acumulador=0;
	
	
	Mientras errorAprox>errorEspec Hacer
		aproxAnterior<-acumulador;
		acumulador<-acumulador + ((x)^(2*iterador+1))/factorial(2*iterador+1);
		aproxActual<-acumulador;
		
		Si iterador==1 Entonces
			Escribir iterador," ",aproxActual," ","----";
		SiNo
			errorAprox<-abs(((aproxActual-aproxAnterior)/aproxActual)*100);
			si errorAprox<0 entonces
				errorAprox<-errorAprox*(-1);
			FinSi
		FinSi
		iterador<-iterador+1;
	FinMientras
	
	Escribir "Resultado: ",acumulador

	Er=redondear(acumulador)-truncar(acumulador)
	Err=Er/acumulador
	Errp=Err*100
	
	Escribir 'Er=',Er
	Escribir 'Err=',Err
	Escribir 'Errp=',Errp,"%"
	
	
FinAlgoritmo