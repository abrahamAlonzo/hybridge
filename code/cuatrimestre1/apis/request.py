import requests
def mostrar_productos():
    productos = requests.get("https://fakestoreapi.com/products").json()
    # id - title - price
    for item in productos:
      print("[{}]: {} - ${}".format(item["id"], item["title"], item["price"] ))

mostrar_productos()