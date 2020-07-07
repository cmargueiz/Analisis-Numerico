from sympy import *

print ("Raices de -9X^4+25X^3-5x^2-26x+24")

a=-25/9
b=5/9
c=26/9
d=-24/9

P=(8*b-3*(pow(a,2)))/8
Q=(8*c-4*a*b+pow(a,3))/8
R=(256*d-64*a*c+16*pow(a,2)*b-3*pow(a,4))/256
print ("2-variables para formar la cubica")

a2=-(P/2)
b2=(R)
c2=((4*P*R)-pow(Q,2))/8

print ("3- Resolver por tartaglia")

p2=b2-pow(a2,2)/3
q2=c2-((a2*b2)/3)+2*pow(a,3)/27

D=(sqrt((4*pow(p2,3)+27*pow(q2,2))/108))
U=0

if (D>0):
	A=-q2/2+sqrt(pow(q2,2)/4+pow(q2,3)/27)
	B=-q2/2-sqrt(pow(q2,2)/4+pow(q2,3)/27)
	U=pow(A,(1/3))+pow(B,(1/3))
elif (D<0):
	cosfi=(((27)^0.5)*q2)/((2*p2)*(-p2)^0.5)
	fi=acos(cosfi)
	U=(2*(-p/3)^0.5)*(cos(fi/3))
else:
	U=2*((-q2/2)^(1/3))

V=sqrt(2*U-P)
W=Q/(-2*V)

x1=complex((V/2)-a/4,+sqrt(pow(V,2)-4*(U-W))/2)
x2=complex((V/2)-a/4,-sqrt(pow(V,2)-4*(U-W))/2)
x3=complex(-(V/2)-a/4,+sqrt(pow(V,2)-4*(U-W))/2)
x4=complex(-(V/2)-a/4,-sqrt(pow(V,2)-4*(U-W))/2)

print ("Raices ")
print (x1)
print (x2)
print (x3)
print (x4)