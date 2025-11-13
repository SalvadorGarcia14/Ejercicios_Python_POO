from producto import Producto
from descuento import Descuento
from cliente import Cliente
from compra import Compra

from typing import List
from datetime import datetime

clientes_logins = [
    Cliente("Sylvanas", "Windrunner", "12345678", 1234),
    Cliente("Thrall", "Orco", "87654321"),
]

productos = [
    Producto("Cerveza Weisse PATAGONIA Botella 730 Cc", 1100),
    Producto("Papas Lays 320Cc", 1700),
    Producto("Coca-Cola 2.5 Ltr", 2500),
]

compras_realizadas:List[Compra] = [
    
]


for cliente in clientes_logins:
    print(cliente)

for producto in productos:
    print(producto)