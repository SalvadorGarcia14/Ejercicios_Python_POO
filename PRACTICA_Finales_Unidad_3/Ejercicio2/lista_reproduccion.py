from video import Video
from typing import List

class ListaReproduccion():
    
    _nro_video_autoincremental = 1
    
    def __init__(self, nombre: str):
        ListaReproduccion._nro_video_autoincremental += 1
        self.__nro = ListaReproduccion._nro_video_autoincremental
        self.__nombre = nombre
        self.__videos: List[Video] = []
    
    @property
    def nro(self) -> int:
        return self.__nro
    
    @property
    def nombre(self) -> str:
        return self.__nombre
    @nombre.setter
    def nombre(self, nuevo_nombre: str) -> str:
        self.__nombre = nuevo_nombre

    @property
    def videos(self) -> List:
        return self.__videos
    
    @property
    def cantidad_videos(self) -> int:
        return len(self.videos)
    
    def add_video(self, video: Video):
        if video not in self.videos:
            self.videos.append(video)
            print("Se agrego el video")
        else:
            print("El video ya existe en la lista")
    
    def remuve_video(self, video: Video):
        if video in self.videos:
            self.videos.remove(video)
            print("Se elimino el video")
        else:
            print("El video no se encuntra en la lista")
    
    
    def __str__(self):
        return (
            f"N°: {self.nro} - Lista de Reproduccion: {self.nombre} | Cant Videos: [{self.cantidad_videos}] \n"
        )
    

