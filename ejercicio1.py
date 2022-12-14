numeros=0
for f in range(5):
    valor=int(input("Ingrese un número:  "))
    if valor!= 0:
        if valor%3==0:
            numeros=numeros+1
print("Cantidad de números ingresados múltiplos de 3: ")
print(numeros)
