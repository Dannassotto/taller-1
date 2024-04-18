import os
nombre= ""
edad=0
peso =0
altura=0
imc=0.0
pesoideal = 0
obesidadgrado1=0
obesidadgrado2=0
obesidadgrado3=0
sobrepeso=0
os . system('cls')
for i in range(0,3,1):
    nombre += (input(f'ingrese el nombre del estudiante {i+1} '))
    edad += float(input(f'ingrese el edad del estudiante {i+1} '))
    if ((edad >=1) and (edad <= 10)):
        print('es un niño')
    elif ((edad > 10) and (edad < 18)):
        print('es un adolocente')
    elif ((edad >= 18) and (edad <= 60)):
        print('es un adulto mayor')
    peso+= float(input(f'ingrese el peso del estudiante {i+1} ')) 
    altura += float(input(f'ingrese el altura del estudiante {i+1} '))
    imc= (peso/(altura * altura))
    if((imc >= 18.5) and (imc <= 24.9)):
        pesoideal += 20
        print('la persona tiene peso normal' ,pesoideal)
    elif((imc >= 25) and (imc <=29.9 )):
        sobrepeso += 20
        print('la persona tiene sobrepeso',sobrepeso)
    elif((imc >= 30) and (imc <= 34.9)):
        obesidadgrado1 += 20
        print('la persona tiene obesidad grado 1') ,obesidadgrado1
    elif((imc >= 35) and (imc <= 39.9)):
        obesidadgrado2 += 20
        print('la persona tiene obesidad grado 2' , obesidadgrado2)
    elif((imc >= 40) and (imc <= 1000)):  
         obesidadgrado3 += 20
         print('la persona tiene obesidad grado 2' , obesidadgrado2)
         print('el imc de los estudiantes son:', imc ) 

print (f"la cantidad de personas con peso normal es de {pesoideal}")
print (f"la cantidad de personas con obecidad 1 es de {obesidadgrado1}")
print (f"la cantidad de personas con obecidad 2 es de {obesidadgrado2}")
print (f"la cantidad de personas con obecidad 3 es de {obesidadgrado2}")
print (f"la cantidad de personas con sobrepeso es de {sobrepeso}")