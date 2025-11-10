

class Localidad:
    def __init__(self, nombre: str, cod_postal: int):
        self.nombre = nombre
        self.cod_postal = cod_postal

    def __str__(self):
        return f"{self.nombre} (Codigo Postal: {self.cod_postal})"