#variables
codigoproducto = 0
productos = []
nombreproducto = 0
valorcomprarproducto = 0
valorventaproducto = 0
stokminimopermitido = 0
stokmaximopermitido = 0
nombreproveedor = 0
rango = 0
eleccion = 0

#actuaclizacion de stok de producto punto numero 3
def encontrar_producto_por_codigo(codigo):
    for producto in productos:
        if producto['codigo'] == codigo:
            return producto
    return None

#informer criticos punto numero 4
def generar_informe_productos_criticos():
    print("Productos con stock por debajo del límite mínimo:")
    for producto in productos:
        if producto['stock_actual'] < int(producto['stock_minimo']):
            print(f"Código: {producto['codigo']}")
            print(f"Nombre: {producto['nombre']}")
            print(f"Stock actual: {producto['stock_actual']}")
            print(f"Stock mínimo permitido: {producto['stock_minimo']}")
            print()

#ganancia potencial punto numeo 5
def calcular_ganancia_potencial_total():
    ganancia_total = 0
    for producto in productos:
        diferencia_valor = float(producto['valor_venta']) - float(producto['valor_compra'])
        ganancia_potencial = diferencia_valor * producto['stock_actual']
        ganancia_total += ganancia_potencial
    return ganancia_total  
#menu
while eleccion != 6:
    print("""
    indique la operacion
    1) registro de productos
    2) visualizacion de productos
    3) actualizacion de stock
    4) informe de productos criticos
    5) calculo de ganancia potencial
    6) salir 
    """)
    eleccion = int(input("\t:)_"))

#introduccion de datos punto numero 1
    if eleccion == 1:
        rango = int(input("ingrese cuantos productos quiere agregar  "))
        for i in range (0,rango):
            codigoproducto = input(f"ingre el codigo del producto {i+1} ") 
            producto = input(f"ingrese el nombre del producto {i+1} ")
            valorcomprarproducto = input(f"ingre el valor de compra del producto {i+1} ") 
            valorventaproducto = input(f"ingrese el valor de venta del producto {i+1} ") 
            stokminimopermitido = input(f"ingrese el stokc minimo permitido {i+1} ")
            stokmaximopermitido = input(f"ingrese el stock maximo permitido {i+1} ")
            nombreproveedor = input(f"ingrese el nombre del proeevedor {i+1} ")
            producto = {
                'nombre': producto,
                'codigo' : codigoproducto,
                'valor_compra': valorcomprarproducto,
                'valor_venta': valorventaproducto,
                'stock_minimo': stokminimopermitido,
                'stock_maximo': stokmaximopermitido,
                'proveedor': nombreproveedor,
                'stock_actual': 0 
            }
            productos.append(producto)

#leer datos punto numero 2
    elif eleccion == 2:
        print("Lista de productos registrados:")
        for idx, producto in enumerate(productos, start=1):
            print(f"Producto {idx}:")
            print(f"Código: {producto['codigo']}")
            print(f"Nombre: {producto['nombre']}")
            print(f"Valor de compra: {producto['valor_compra']}")
            print(f"Valor de venta: {producto['valor_venta']}")
            print(f"Stock mínimo permitido: {producto['stock_minimo']}")
            print(f"Stock máximo permitido: {producto['stock_maximo']}")
            print(f"Proveedor: {producto['proveedor']}")
            print(f"Stock actual: {producto['stock_actual']}")
            print()

#actuzalizacion de stock punto numero 3
    if eleccion == 3:
        codigo = input("Ingrese el código del producto: ")
        cantidad = int(input("Ingrese la cantidad a agregar/restar al stock: "))
        producto = encontrar_producto_por_codigo(codigo)
        if producto:
            producto['stock_actual'] += cantidad
            print(f"Stock actualizado para el producto {producto['nombre']}. Nuevo stock: {producto['stock_actual']}")
        else:
            print("¡Producto no encontrado!")
    
#critico punto numero 4
    if eleccion == 4:
        generar_informe_productos_criticos()

#ganancias punto numero 5
    if eleccion == 5:
        ganancia_total = calcular_ganancia_potencial_total()
        print(f"La ganancia potencial total es: {ganancia_total}")
#salir
    if eleccion == 6:
        print ("gracias por utulizar el programa")