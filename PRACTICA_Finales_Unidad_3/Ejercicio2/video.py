from tag import Tag
from usuario import Usuario

from typing import List
from datetime import date


class Video():
    def __init__(self, nombre: str, fecha_publicacion: date, usuario: Usuario):
        self.__nombre = nombre
        self.__fecha_publicacion = fecha_publicacion
        self.__usuario = usuario
        self.__palabras_claves: List[Tag] = []
    
    @property
    def nombre(self) -> str:
        return self.__nombre
    @nombre.setter
    def nombre(self, nuevo_nombre: str) -> str:
        self.__nombre = nuevo_nombre

    @property
    def fecha_publicacion(self) -> date:
        return self.__fecha_publicacion

    @property
    def usuario(self) -> Usuario:
        return self.__usuario 

    @property
    def palabras_claves(self) -> List:
        return self.__palabras_claves

    def add_tag(self, tag: Tag):
        if tag not in self.palabras_claves:
            self.palabras_claves.append(tag)
        else:
            print("El tag ya existe")

    def remove_tag(self, tag: Tag):
        if tag in self.palabras_claves:
            self.palabras_claves.remove(tag)
        else:
            print("El tag no se encuentra")
    
    
    def __str__(self):
        tags = ",".join(str(tag) for tag in self.palabras_claves) if self.palabras_claves else "Sin Tags"
        
        return (
            f"Video: {self.nombre} - Fecha: {self.fecha_publicacion.strftime("%d/%m/%Y")} \n"
            f"Tags: {tags} \n"
            f"Usuario: {self.usuario} \n"
        )