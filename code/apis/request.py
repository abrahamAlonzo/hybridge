import requests
def mostrar_productos():
    productos = requests.get("https://fakestoreapi.com/products").json()
    # id - title - price
    print("[{}]: {} - ${}".format(productos[0]["id"], productos[0]["title"], productos[0]["price"] ))

mostrar_productos()