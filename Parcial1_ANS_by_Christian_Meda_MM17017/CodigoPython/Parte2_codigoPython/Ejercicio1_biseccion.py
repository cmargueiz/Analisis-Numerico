from sympy import *

def f(num):
	return (sin(num)-6*num-5)

x1=-2
x2=-0.9

errorAproximado=1
errorEspecifico=0.05
iterador=1
condicion=""
anterior=0
actual=0

if (f(x1)*f(x2)<0):
	print "Valores Validos"
	print "i | x1 | x2 | xr | fx1 | fx2 | fxr | fx1*fxr | condicion | EA"
	xr=(x1+x2)/2
	if f(x1)*f(xr)<0:
		condicion="<"
	elif f(x1)*f(xr)>0:
		condicion=">"

	print iterador," | ",x1," | ",x2," | ",xr," | ",f(x1)," | ",f(x2)," | ",f(xr)," | ",f(x1)*f(xr)," | ",condicion," | ",errorAproximado

	if f(x1)*f(xr)<0:
		x2=xr
		condicion="<"
	elif f(x1)*f(xr)>0:
		condicion=">"
		x1=xr
	else:
		print "La raiz es: ",xr
		errorAproximado=0

	while errorAproximado>errorEspecifico:
		anterior=xr
		xr=(x1+x2)/2
		actual=xr
		fx1=f(x1)
		fx2=f(x2)
		fxr=f(xr)
		if f(x1)*f(xr)<0:
			x2=xr
			condicion="<"
		elif f(x1)*f(xr)>0:
			condicion=">"
			x1=xr
		else:
			print "La raiz es: ",xr
			break

		if (iterador!=1):
			errorAproximado=Abs((anterior-actual)/actual)*100

		print iterador," | ",x1," | ",x2," | ",xr," | ",fx1," | ",fx2," | ",fxr," | ",fx1*fxr," | ",condicion," | ",errorAproximado
		iterador=iterador+1
else:
	print "Valores invalidos"		

print "La raiz es: ",xr
print "EA: ",errorAproximado