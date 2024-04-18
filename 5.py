Ciudad_1=""
Ciudad_2=""
Ciudad_3=""
Ciudad_4=""
Ciudad_5=""
sis1=0
sis2=0
sis3=0
sis4=0
sis5=0
op=0
print('menu')
while op != 5: 
    print('1.registrar ciudad\n2.registra sismo\n3.buscar sismos por ciudad\n4.informe riesgo\n5.Salir') 
    op = int(input('Ingresa una opcion: ')) 
    
    if op == 1:
        Ciudad_1= input('ingrese ciudad #1 >')
        Ciudad_2= input('ingrese ciudad #2  >')
        Ciudad_3= input('ingrese ciudad #3  >')
        Ciudad_4= input('ingrese ciudad #4 >') 
        Ciudad_5= input('ingrese ciudad #5 >')
    elif op == 2:
        sis1=+ float(input(f'ingresa la intensidad del sismo de la  {Ciudad_1} >'))
        sis2=+ float(input (f'ingrese la intensidad del sismo de la {Ciudad_2} > '))
        sis3=+ float(input (f'ingrese la intensidad del sismo de la {Ciudad_3} >'))
        sis4=+ float(input (f'ingrese la intensidad del sismo de la {Ciudad_4} >'))
        sis5=+ float(input (f'ingrese la intensidad del sismo de la {Ciudad_5} >'))
    elif op == 3:
         print(f' la intensidad del sismo en {Ciudad_1} es > {sis1}')
         print(f' la intensidad del sismo en {Ciudad_2} es > {sis2}')
         print(f' la intensidad del sismo en {Ciudad_3} es > {sis3}')
         print(f' la intensidad del sismo en {Ciudad_4} es > {sis4}')
         print(f' la intensidad del sismo en {Ciudad_5} es > {sis5}')
    elif op == 4:
        if((sis1 <= 2.5)): 
             print(f'amarillo)sin riesgo en {Ciudad_1}') 
        elif((sis1 >= 2.6)and (sis1 <= 4.5)):
             print(f'naranja)riesgo medio en {Ciudad_1}')
        elif((sis1> 4.5)):
             print(f'rojo)riesgo alto en {Ciudad_1}')

        if ((sis2 <= 2.5)):
            print(f'amarillo)sin riesgo en {Ciudad_2}')
        elif((sis2 >= 2.6)and (sis2<= 4.5)):
            print(f'naranja)riesgo medio en {Ciudad_2}'),
        elif((sis2> 4.5)):
           print(f'rojo)riesgo alto en {Ciudad_2}')

        if (sis3 <= 2.5): 
           print(f'amarillo)sin riesgo en {Ciudad_3}')
        elif((sis3 >= 2.6)and (sis3 <= 4.5)):
           print(f'naranja)riesgo medio en {Ciudad_3}')
        elif((sis3 > 4.5)):
           print(f'rojo)riesgo alto en {Ciudad_3}')

        if ((sis4 <= 2.5)):
           print(f'amarillo)sin riesgo en {Ciudad_4}') 
        elif((sis4 >= 2.6)and (sis4<= 4.5)):
           print(f'naranja)riesgo medio en {Ciudad_4}')
        elif((sis4 > 4.5)):
           print(f'rojo)riesgo alto en {Ciudad_4}')

        if ((sis5 <= 2.5)): 
           print(f'amarillo)sin riesgo en {Ciudad_5}')
        elif((sis5 >= 2.6)and (sis5 <= 4.5)):
           print(f'naranja)riesgo medio en {Ciudad_5}')
        elif((sis5 > 4.5)):
           print(f'rojo)riesgo alto en {Ciudad_5}')
    elif op == 5:
       print('salir')
    

