#Ejercicio 1
print("-------------------------Ejercicio #1-------------------------")
contraseña=str(input("Ingrese Una Contraseña: "))
control=0
nuevaContraseña=""
while(control!=1):
    nuevaContraseña=str(input("Ingrese De Nuevo La Contraseña: "))
    if contraseña==nuevaContraseña:
        print("La Contraseña Es Correcta")
        control=1
    else:
        print("La Constraseña Es Incorrecota")
#Ejercicio 2
print("-------------------------Ejercicio #2-------------------------")       
nombre=str(input("Ingrese Su Nombre: ").upper())
genero=str(input("Ingrese h Si Es Hombre, m Si Es Mujer: ").upper())
primeraLetra=nombre[0]
if (genero=="H"):
    if(primeraLetra>"N"):
        print("Pertenece Al Grupo A")
    else:
        print("Pertenece Al Grupo B")
elif(genero=="M"):
    if(primeraLetra<"M"):
        print("Pertenece Al Grupo A")
    else:
        print("Pertenece Al Grupo B")