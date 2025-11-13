from producto import Producto
from descuento import Descuento
from cliente import Cliente

from typing import List
from datetime import datetime

class Compra():
    def __init__(self, fecha_hora: datetime, cliente: Cliente, compra_facturada: bool, monto_facturado: float, descuento: Descuento = None):
        self.__fecha_hora = fecha_hora
        self.__cliente = cliente
        self.__compra_facturada = compra_facturada
        self.__monto_facturado = monto_facturado
        self.__productos: List[Producto] = []
        if descuento is None:
            descuento = Descuento(30)
        self.__descuento = descuento

    @property
    def fecha_hora(self) -> datetime:
        return self.__fecha_hora

    @property
    def cliente(self) -> Cliente:
        return self.__cliente


    @property
    def compra_facturada(self) -> bool:
        return self.__compra_facturada
    @compra_facturada.setter
    def compra_facturada(self, nuevo_compra_facturada) -> bool:
        self.__compra_facturada = nuevo_compra_facturada
        
    @property
    def monto_facturado(self) -> float:
        return self.__monto_facturado
    @monto_facturado.setter
    def monto_facturado(self, nuevo_monto_facturado) -> float:
        self.__monto_facturado= nuevo_monto_facturado
    
    @property
    def descuento(self) -> Descuento:
        return self.__descuento

    @property
    def productos(self):
        return self.__productos
    @property
    def cantidad_productos(self) -> int:
        return len(self.__productos)


    @property
    def monto_total(self) -> float:
        total = 0
        for producto in self.productos:
            total += producto.precio_unitario
        return total

    def finalizar_compra(self):
        monto_final = self.monto_total

        if self.cliente.nro_comunidad is not None and isinstance(self.descuento, Descuento):
            monto_final -= self.descuento.calcular_monto_descuento_comunidad(monto_final)

        self.compra_facturada = True
        self.monto_facturado = round(monto_final, 2)
    
    def add_producto(self, producto: Producto):
        self.__productos.append(producto)
    
    def remove_producto(self, producto: Producto):
        if producto in self.__productos:
            self.__productos.remove(producto)
    
    def __str__(self):
        return (
            f"{self.fecha_hora.strftime('%d/%m/%Y %H:%M')} hs \n"
            f"Monto: {self.monto_total} - Productos: [{self.cantidad_productos}] \n"
            f"Cliente: {self.cliente} \n"
        )