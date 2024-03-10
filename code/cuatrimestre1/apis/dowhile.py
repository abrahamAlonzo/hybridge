# escribe tu código aquí
productos = [
    {
        "sku": 1,
        "nombre": "Coca Cola",
        "precio": 15
    },
    {
        "sku": 2,
        "nombre": "Gansito",
        "precio": 20
    },
    {
        "sku": 3,
        "nombre": "Paketaxo",
        "precio": 60
    },
]

def buscar_producto(sku):
    #busca el producto con sku en la lista de diccionarios `productos`
    for product in productos:
        if product["sku"] == sku:
            return product


value = buscar_producto(3)
print(value)