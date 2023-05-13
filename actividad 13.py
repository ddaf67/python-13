#-*-coding:utf-8-*-

#Decoración:Nombre del Algoritmo
print("-------------------------------------------------------")
print("Complemento3:COSTO DE ARTICULO.")
print("-------------------------------------------------------")

#Entradas
print("Ingrese el Costo del articulo:")
costo=float(input())

print("Ingrese la marca:")
#m no necesita conversion ya que la entrada son texto
m=input()


#Proceso
if costo>=2000 and m=="NOSY":
   pa=costo*0.90
   pt=pa*0.95

elif costo>=2000 and m !="NOSY":
   pt=costo*0.90

elif costo<2000 and m=="NOSY":
   pa=costo*0.95
   pt=pa+pa*0.20

elif costo<2000 and m !="NOSY":
   pa=costo*1.20


#Salida
print("/nSALIDA:")
print("-------------------------------------------------------")
print("Usted pagara:",pa,"soles")
