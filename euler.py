#############################################
#Calculo aporoximacion euler		    #
#Luis Venegas Leiva 2019079322	      	    #
#Ultima modificacion: 7/09/2020 19:22	    #
#############################################

def e_cuadratica(n):
	suma=float(1)
	contador=float(1)
	factorial=float(1)
	if n==1:
		print (suma)
	elif n==2:
		print (suma+1)
	else:
		suma=2
		for i in range(2,n):
			while contador<i:
				factorial=factorial*(contador+1)
				contador =contador+1
			suma = suma+(1/factorial)
			factorial=1.0
			contador=1.0
		#print(suma)
		return suma


def e_lineal(n):
	factorial=float(1)
	suma=float(1)
	if n==1:
		print (suma)
	elif n==2:
		print (suma+1)
	else:
		suma=2
		for i in range (2,n):
			factorial=factorial*i
			suma=suma+(1/factorial)
		#print(suma)
		return suma

#e_cuadratica(50)
#e_lineal(50)
