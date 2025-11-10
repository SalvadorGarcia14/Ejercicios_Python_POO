from pais import Pais
from provincia import Provincia
from localidad import Localidad
from cliente import Cliente

from typing import List
from datetime import date

# Cargar paises
argentina = Pais("Argentina")
italia = Pais("Italia")

#Cargar Provincias
santa_fe = Provincia("Santa Fe")
bs_as = Provincia("Buenos Aires")

emilia_romagnia = Provincia("Emilia-Romagna")
lombardia = Provincia("Lombardia")

#Cargar Localidades

rosario = Localidad("Rosario", 2000)
funes = Localidad("Funes", 2132)

la_plata = Localidad("La Plata", 1900)
ciudad_autonoma_bs_as = Localidad("Ciudad Autonoma de Buenos Aires", 1000)


bolonia = Localidad("Bolonia", 5555)
milan = Localidad("Milan", 2222)

# Relacionar provincias con localidades

santa_fe.add_localidad(rosario)
santa_fe.add_localidad(funes)

bs_as.add_localidad(la_plata)
bs_as.add_localidad(ciudad_autonoma_bs_as)

emilia_romagnia.add_localidad(bolonia)
lombardia.add_localidad(milan)

# Relacionar paises con provincias
argentina.add_provincia(santa_fe)
argentina.add_provincia(bs_as)

italia.add_provincia(emilia_romagnia)
italia.add_provincia(lombardia)


paises: List[Pais] = [argentina, italia]

clientes: List[Cliente] = [
    Cliente("Anna Zak", "Paraguay 1460", rosario, date(2024, 10, 22)),
    Cliente("Sylvanas Windrunner", "Milano 888", milan, date(2025, 5, 10)),
    Cliente("Yorha Modelo 2B", "Pelegrinni 2345", ciudad_autonoma_bs_as, date(2022, 4, 10), date(2023, 12, 1)),
]