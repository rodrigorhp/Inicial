#A00827198 Rodrigo Henriquez
#A00827838 Luis Angel Mendoza Castillón
#proposito del programa
#Calcular area y perimetro de un rectangulo

#funcion1  calcular área del rectángulo
def calcularArea(l1, l2):
    return (l1 * l2)

#funcion2  calcular perímetro del rectángulo
def calcularPerimetro(l1,l2):
    return(2*l1+2*l2)

#instrucciones de accion
#pedir datos
print("medida de lado 1 del rectángulo")
l1 = float(input())

print("medida de lado 2 del rectángulo")2
l2 = float(input())

#desplegar calculo funcion1
area = calcularArea(l1,l2)
print(area)
#desplegar calculo funcion 2
perimetro = calcularPerimetro(l1,l2)
print(perimetro)
