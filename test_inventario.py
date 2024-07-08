from inventario import Inventario

def test_agregar_producto_exitoso():
    inventario = Inventario()
    resultado = inventario.agregar_producto("Producto1", 10, 100)
    assert resultado == True
