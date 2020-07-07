Proceso Ejercicio3
	Dimension  matrizA(2,2), matrizX(2,2), matrizY(2,2);
	Definir  matrizA,matrizX,matrizY,x,ye,determinante, deterX,deterY como real;
	matrizA[0,0]<-21.76;
	matrizA[0,1]<-24.34;
	matrizA[1,0]<-14.16;
	matrizA[1,1]<-15.84;
	
	matrizX[0,0]<-1.24;
	matrizX[0,1]<-24.34;
	matrizX[1,0]<-1.15;
	matrizX[1,1]<-15.84;
	
	matrizY[0,0]<-21.76;
	matrizY[0,1]<-1.24;
	matrizY[1,0]<-14.16;
	matrizY[1,1]<-1.15;
	
	
	determinante<-matrizA[0,0]*matrizA[1,1]-matrizA[0,1]*matrizA[1,0];
	
	deterX<-matrizX[0,0]*matrizX[1,1]-matrizX[0,1]*matrizX[1,0];
	
	deterY<-matrizY[0,0]*matrizY[1,1]-matrizY[0,1]*matrizY[1,0];
	
	x<-((deterX/determinante));
	ye<-deterY/determinante;
	
	escribir "x=",x;
	escribir "y=",ye;
	
	
	
FinProceso
