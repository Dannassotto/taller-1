n = 0
totalnumeros = 0
npar = 0
nimpar = 0
m10=0
entre20y50=0
may100=0
sumapar=0
sumaimpar=0

n = int(input("Ingrese un número: "))

if n < 0:
    print('Ingresó un número negativo. La ejecución se detuvo.')
else:
    while True:  
        if n % 2 == 0:
            print(f'El número {n} es par')
            npar += 1 
            sumapar += n
            promediopares=sumapar/npar
        else:
            print(f'El número {n} es impar')
            nimpar += 1
            sumaimpar += n
            promedioimpares=sumaimpar/nimpar
        totalnumeros += 1

        if ((n >=1) and (n <= 10)): 
             print('es menor de 10 ')
             m10 += 1
 
        elif((n > 20) and (n < 50)):
             print('estan entre 20 y 50')
             entre20y50 += 1
        elif((n> 100)):
             print('este numero es mayores de 100')
             may100 += 1
        else:
             print ('valor no sopotado por el programa ') 
        
        n = int(input("siguiente numero(agrega un número negativo para salir): "))
        if n < 0:
            print("se ingreso un número negativo la ejecucion se detuvo")
            break 
    
print('El total de números:', totalnumeros)
print('números pares ingresados:', npar)
print('promedio de numeros pares ingresado:',promediopares)
print('números impares ingresados:', nimpar)
print('promedio de numeros impares ingresado:',promedioimpares)
print('son menores a 10:', m10)
print('estan entre 20 y 50:' , entre20y50)
print('son mayores de 100:',may100)
