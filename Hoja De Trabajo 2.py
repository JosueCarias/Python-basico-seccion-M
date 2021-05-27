#Ejercicio 1
tamaño=int(input("Ingrese un numero entero positivo: "))
acumulador=""
if tamaño<=0:
    print("El numero ingresado no es un numero entero positivo")
else:
    for x in range (tamaño+1):
        print(acumulador)
        acumulador+="*"
#Ejercicio 2
numero=int(input("Ingrese Un Numero Positvo: "))
acomulador=""
if numero<0:
    print("El Numero No es un entero postivo")
else:
    for x in range(numero):
        acomulador+=str(numero)+","
        numero-=1
acomulador+="0"
print(acomulador)
#Ejercicio 3
numero=int(input("Ingrese un numero a consultar: "))
constante=2
if numero ==1:
    print("El numero no es primo")
elif numero==2:
    print("Es Un numero primo")
elif numero>2:
    while numero % constante !=0:
        constante+=1
    if constante==numero:
        print("Es Un Numero Primo")
    else:
        print("No es Un Numero Primo")