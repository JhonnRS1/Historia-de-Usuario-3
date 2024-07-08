
class Inventario:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, nombre, cantidad, precio):
        producto = {"nombre": nombre, "cantidad": cantidad, "precio": precio}
        self.productos.append(producto)
        return True

    def mostrar_inventario(self):
        print("Inventario:")
        for producto in self.productos:
            print(f"Nombre: {producto['nombre']}, Cantidad: {producto['cantidad']}, Precio: {producto['precio']}")
