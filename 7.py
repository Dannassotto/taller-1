productos = []
nproducto = input("Ingrese el nombre del producto: ")
def encontrar_por_codigo(codproducto):
    for producto in productos:
        if producto['codigo'] == codproducto:
            return producto

while True:
    print('1. Registro de producto\n2. Visualización de productos\n3. Actualización de stock\n4. Informe de producto críticos\n5. Cálculo de ganancia potencial\n6. Salir') 
    op = int(input('Ingresa una opción: ')) 
    
    if op == 1:
        codproducto = input("Ingrese el código producto: ") 
        vcompra = float(input("Ingrese el valor de compra: "))
        vventa = float(input("Ingrese el valor de venta: "))
        stockmn = int(input("Ingrese el stock mínimo: "))
        stockmy = int(input("Ingrese el stock máximo: "))
        nprovedor = input("Ingrese el nombre del proveedor: ")
        productos.append({
            'codigo': codproducto,
            'nombre': nproducto,
            'valor_compra': vcompra,
            'valor_venta': vventa,
            'stock_minimo': stockmn,
            'stock_maximo': stockmy,
            'proveedor': nprovedor,
            'stock_actual': 0 
        })
    elif op == 2:
        print("Listado de productos:")
        for producto in productos:
            print(f"Código: {producto['codigo']}")
            print(f"Nombre: {producto['nombre']}")
            print(f"Proveedor: {producto['proveedor']}")
            print(f"Valor de compra: {producto['valor_compra']}")
            print(f"Valor de venta: {producto['valor_venta']}")
            print(f"Stock mínimo: {producto['stock_minimo']}")
            print(f"Stock máximo: {producto['stock_maximo']}")
            print(f"Stock actual: {producto['stock_actual']}")
            print("")
    elif op == 3:
        codproducto = input("Ingrese el código del producto: ")
        cantidad = int(input("Ingrese la cantidad a agregar/restar al stock: "))
        producto = encontrar_por_codigo(codproducto)
        if producto:
            producto['stock_actual'] += cantidad
            print(f"Stock actualizado para el producto {producto['codigo']}. Nuevo stock: {producto['stock_actual']}")
        else:
            print("Producto no encontrado")
    elif op == 4:
        print('Productos con stock por debajo del mínimo:')
        for producto in productos:
            if producto['stock_actual'] < producto['stock_minimo']:
                print(f'Código: {producto["codigo"]}, Proveedor: {producto["proveedor"]}, Stock actual: {producto["stock_actual"]}')
    elif op == 5:
        tganancia = 0
        for producto in productos:
            gpotencial = (producto['valor_venta'] - producto['valor_compra']) * producto['stock_actual']
            tganancia += gpotencial
        print(f'La ganancia potencial total es: {tganancia}')
    elif op == 6:
        break