from sympy import *
from math import *
def solucion():

	print "Solucion para -x^3+2x^2+x-1=0, pero dividimos toda la ecuacion por -1"
	print "ecuacion a resolver -x^3+2x^2+x-1=0"

	errorAproximado=1
	errorEspecifico=0.05
	a=-2
	b=-1
	c=1
	k=-a/3
	p=b-pow(a,2)/3
	


	q=c-(a*b)/3+(2*(pow(a,3)/27))

	D=(4*pow(p,3)+27*pow(q,2))/108

	if D>0:
		A=-q/2+sqrt(pow(q,2)/4+pow(q,3)/27)
		B=-q/2-sqrt(pow(q,2)/4+pow(q,3)/27)
		x1=pow(A,(1/3))+pow(B,(1/3))
		x2=-(pow((A),(1/3))+pow((A),(1/3)))/2+pow(3,(1/3))*(pow((A),(1/3))-pow((A),(1/3)))/2
		x3=-(pow((A),(1/3))+pow((A),(1/3)))/2-pow(3,(1/3))*(pow((A),(1/3))-pow((A),(1/3)))/2
	elif D<0:
		cosfi=((sqrt(27))*q)/((2*p)*(sqrt(-p)))
		fi=acos(cosfi)
		
		x1=(2*sqrt(-p/3))*(cos(fi/3))+k
		x2=(2*sqrt(-p/3))*(cos(fi/3+(2*pi/3)))+k
		x3=(2*sqrt(-p/3))*(cos(fi/3+(4*pi/3)))+k


	else:
		x1=2*pow((-(q/2)),(1/3))+k
		x2=pow((q/2),(1/3))+k
		x3=pow((q/2),(1/3))+k


	print "Las raices son: \n"
	print x1
	print x2
	print x3
solucion()