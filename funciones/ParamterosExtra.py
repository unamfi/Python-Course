"""#Recibe un numero n de parametros
#Lo recibe como una tupla
def suma3(a=0,b=0,*variablesExtra):
	suma=0
	for x in variablesExtra:
		suma = suma+x #suma += x
	return suma+a+b
a=10
b=20
c=30
d=40
e=50

print(suma3())
print(suma3(1))
print(suma3(c,d))
print(suma3(a,b,c))
print(suma3(a,b,c,d,e,30))

#Pasar parametros extra como diccionarios
def muestraDic(a=0,b=0,**llavevalor):
	if llavevalor is not None:
		for llave,valor in llavevalor.items(): #.keys() .values()
			print("Llave: ",llave,"Valor: ",valor)
muestraDic(4)
muestraDic(1,2,nombre="Jorge",fruta="Manzana",color="Verde")
"""
def nombres(mio='Jorge',*amigos,**mejoresAmigos):
	numAmigos=0
	numMejoresAmigos=0
	print("Mi nombre es: ",mio)
	if mejoresAmigos: #mejoresAmigos= None ---> if None ---> False
		for llave,valor in mejoresAmigos.items():
			print("Mi mejor amigo de %s es %s"%(llave,valor))
			numMejoresAmigos+=1
	print("Y mis amigos son:")
	if amigos:
		for amigo in amigos:
			print(str(numAmigos)+".- ",amigo)
			numAmigos+=1
	if numAmigos== 0 and numMejoresAmigos==0:
		print("No tengo amigos :'(")

nombres()
print("---------------")
nombres("David","Carlos","Ana","Maria")
print("---------------")
nombres("David",facultad="jose",trabajo="Ana")
print("---------------")
nombres("David","Edgar","Adrian",facultad="Jose",trabajo="Ana")
