supermercado = {}

print("Ingrese un producto (presione enter para terminar ingreso)")
while True:
    print("Ingrese un producto (presione enter para terminar ingreso)")
    producto = input("Ingrese el nombre del producto: ")
    if producto == "":
        break
    cantidad = int(input("Ingrese la cantidad del producto: "))
    supermercado[producto] = cantidad

x = int(input("Ingrese un valor para multiplicar los productos: "))
print("\nProductos con cantidades multiplicadas por", x, ":")
for producto, cantidad in supermercado.items():
    cantidad_multiplicada = cantidad * x
    print(f"{producto}: {cantidad_multiplicada}")