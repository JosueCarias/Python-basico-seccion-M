peso=float(input("Ingrese Su Peso En Kilogramos: "))
altura=float(input("Ingrese Su Altura En Metros: "))
imc=round(peso/(altura**2),2)
print("Tu Indice De Masa Corporal Es: "+str(imc))
