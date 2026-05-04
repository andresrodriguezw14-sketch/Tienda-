import random 
import os

class Producto:
    nombre: str = False
    precio: int = 0
    stock: int = 0

    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        self.total = 0
        print("El producto se creó exitosamente...")

    def vender_producto(self, nombre, cantidad):
        if self.nombre == nombre:
            if self.stock >= cantidad:
                self.stock -= cantidad
                self.total = cantidad * self.precio
                print("Venta exitosa....")
                print(f"Total de la compra ${self.total:,.0f}")
            else:
                print("No tenemos stock suficiente")
        else:
            print("El producto no existe")

    def consultar_stock(self, nombre):
        if self.nombre == nombre:
            print(f"El producto {self.nombre} existe y su estock {self.stock} productos en inventario")
        else:
            print(f"El producto con nombre: {nombre}, no existe ")

    def limpiar_pantalla():
        os.system('cls' if os.name == 'nt' else 'clear')

    def reducir_stock(self, nombre, cantidad):
        if self.nombre == nombre:
            if self.stock >= cantidad:
                self.stock -= cantidad
                print("Reducción exitosa....")
                print(f"El stock quedo en {self.stock}")
            else:
                print("No tenemos stock suficiente para la reducción")
        else:
            print("El producto no existe")

    def aplicar_descuento(self):
        if self.total == 0:
            print("Primero debe hacer una venta para aplicar descuento")
            return
        desc = random.randint(0, 100)
        sub = self.total * desc / 100
        print(f"Su descuesto es de {desc:,.0f} %")
        print(f"Total compra: ${self.total:,.0f}")
        print(f"Total descontado: ${sub:,.0f}")
        print(f"Total a pagar: ${self.total - sub:,.0f}")

    def mostrar(self):
        print(f"Nombre: {self.nombre}")
        print(f"Precio: {self.precio:,.0f}")
        print(f"Cantidad: {self.stock}")

    def disponibidad(self, nombre):
        if self.nombre == nombre:
            if self.stock > 0:
                print(f"El producto {nombre} tiene una disponibilidad de {self.stock} unidades")
            else:
                print(f"El producto {nombre} no tiene disponibilidad")
        else:
            print(f"El producto {nombre} no existe")

while True:
    Producto.limpiar_pantalla()
    opc = int(input(">>> Bienvenidos a la tienda de Yulibeth <<<\nMenú\n1. Agregar\n2. Vender\n3. Consultar\n4. Reducir\n5. Probar suerte\n6. Mostrar\n7. Disponibilidad\n8. Salir\n\nPor favor escriba su opcion: "))
    match opc:
        case 1:
            nom = input("Escriba el nombre del producto que desea agregar: ")
            precio = int(input("Escriba el precio del productor: "))
            cant = int(input("Escriba la cantidad del stock: "))
            pro = Producto(nom, precio, cant)
            input("Precione enter para continuar")
        case 2:
            nom = input("Escriba el nombre del producto que desea comprar: ")
            cant = int(input("Escriba la cantidad a comprar: "))
            pro.vender_producto(nom, cant)
            input("Precione enter para continuar")
        case 3:
            nom = input("Escriba el nombre del producto que desea consular stock: ")
            pro.consultar_stock(nom)
            input("Precione enter para continuar")
        case 4:
            nombre = input("Escriba el nombre del producto que desea reducir el stock: ")
            cantidad = int(input("Cantidad que desea reducir en el stock: "))
            pro.reducir_stock(nombre, cantidad)
            input("Precione enter para continuar")
        case 5:
            pro.aplicar_descuento()
            input("Precione enter para continuar")
        case 6:
            pro.mostrar()
            input("Precione enter para continuar")
        case 7:
            nombre = input("Escriba el nombre del producto a verificar: ")
            pro.disponibidad(nombre)
            input("Precione enter para continuar")
        case 8:
            print("...Vuelva pronto...")
            break
print("Gracias por su visita ")
