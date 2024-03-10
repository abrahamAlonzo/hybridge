# Sistema de punto de venta para Abarrotes "El Hybridge"
opc = 0        #opción del menú
carrito = []    #carrito de compras
productos = [
    {
        "sku": 1128,
        "producto": "Coca Cola",
        "precio": 15
    },
    {
        "sku": 8381,
        "producto": "Gansito",
        "precio": 20
    },
    {
        "sku": 3762,
        "producto": "Paketaxo",
        "precio": 60
    },
]

OPCIONES = {
    'MOSTRAR_CARRITO': 1,
    'MOSTRAR_PRODUCTOS': 2,
    'AGREGAR_PRODUCTO': 3,
    'MODIFICAR_PRODUCTO': 4,
    'ELIMINAR_PRODUCTO': 5,
    'SALIR': 6
}


def buscar_producto(sku):
    #busca el producto con sku en la lista de diccionarios `productos`
    for product in productos:
        if product["sku"] == sku:
            return product
    print("Producto no encontrado")

def mostrar_cuenta_actual():
    print("\tCuenta")
    variable = 1
    subtotal = 0
    for producto in carrito:
        print("\t {}) {}: ${}".format(variable, producto["producto"], producto["precio"]))
        variable = variable + 1
        subtotal = producto["precio"] + subtotal
    print("\t======================")
    print("\tSubtotal: ${}".format(subtotal))

def mostrar_productos():
    for p in productos:
        print("SKU: {} | Nombre: {} | Precio: ${}".format(p["sku"], p["producto"], p["precio"]))
        
def agregar_producto():
    # encontrar el producto que tenga el SKU brindado por el usuario
    print(
        "Ingrese el SKU del producto que desea agregar al carrito (0 para terminar): "
    )
    sku = int(input())
    producto = buscar_producto(sku)
    if producto:
        carrito.append(producto)

def eliminar_producto():
    print("Ingrese el SKU del producto que desea eliminar del carrito: ")
    sku = int(input())
    producto = buscar_producto(sku)
    if producto:
        carrito.remove(producto)

def modificar_producto():
    print("Ingrese el SKU del producto que desea modificar del carrito: ")
    sku = int(input())
    producto = buscar_producto(sku)
    if producto:
        productos.remove(producto)
        print("Ingrese el nuevo SKU del producto: ")
        sku = int(input())
        print("Ingrese el nuevo nombre del producto: ")
        nombre = input()
        print("Ingrese el nuevo precio del producto: ")
        precio = float(input())
        new_product = {
            "sku": sku,
            "producto": nombre,
            "precio": precio
        }
        if producto:
            productos.append(new_product)

def mostrar_menu():
    for i in range(1):
        print("==============================================================================================")
    print("===========================Bienvenido a Abarrotes \"El Hybridge\"===============================")
    for i in range(1):
        print("==============================================================================================")
    print("\t\t Menú de opciones")
    print("1) Mostrar Carrito")
    print("2) Mostrar productos")
    print("3) Agregar producto")
    print("4) Modificar producto")
    print("5) Eliminar producto")
    print("6) Salir")
    print("==============================================================================================")

def mostrar_cuenta_actual():
    print("\tCuenta")
    variable = 1
    subtotal = 0
    for producto in carrito:
        print("\t {}) {}: ${}".format(variable, producto["producto"], producto["precio"]))
        variable = variable + 1
        subtotal = producto["precio"] + subtotal
    print("\t======================")
    print("\tSubtotal: ${}".format(subtotal))


def mostrar_puntos_venta():
    mostrar_cuenta_actual()



while opc != OPCIONES['SALIR']:
    mostrar_menu()
    opc = int(input("Opción: "))
    if opc == OPCIONES['MOSTRAR_CARRITO']:
      mostrar_puntos_venta()
    elif opc == OPCIONES['MOSTRAR_PRODUCTOS']:
      mostrar_productos()
    elif opc == OPCIONES['AGREGAR_PRODUCTO']:
      agregar_producto()
    elif opc == OPCIONES['MODIFICAR_PRODUCTO']:
      modificar_producto()
    elif opc == OPCIONES['ELIMINAR_PRODUCTO']:
      eliminar_producto()