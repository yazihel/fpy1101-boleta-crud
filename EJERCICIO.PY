boleta = []

def agregar_producto(nombre, precio):
    producto = {"nombre": nombre, "precio": precio}
    boleta.append(producto)
    print(F"producto '{nombre}' agregado correctamente. ")

def calcular_total():
    total = 0
    for producto in boleta:
        total = total + producto["precio"]
        return total
    
def mostrar_boleta():
    if len(boleta) == 0:
        print("la boleta esta vacia.")

    else:
        print("\n------ BOLETA ------")
        for producto in boleta:
            print(f"  {producto['nombre']}  -  ${producto['precio']}")
        print(f"  TOTAL: ${calcular_total()}")
        print("--------------------\n")

def actualizar_precio(nombre, nuevo_precio):
    for producto in boleta:
        if producto["nombre"] == nombre:
            producto["precio"] = nuevo_precio
            print(f"Precio de '{nombre}' actualizado a ${nuevo_precio}.")
            return
    print(f"Producto '{nombre}' no encontrado.")


actualizar_precio("Leche", 1350)

def eliminar_producto(nombre):
    for producto in boleta:
        if producto["nombre"] == nombre:
            boleta.remove(producto)
            print(F"producto '{nombre}' eliminado correctamente.")
            return
        print(F"producto '{nombre}' no encontrado.")
   
agregar_producto("galleta", 1500)
agregar_producto("bebida", 1700)

actualizar_precio("galleta", 990)