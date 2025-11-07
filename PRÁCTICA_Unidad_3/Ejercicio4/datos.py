from estadia import Estadia
from precio import Precio

from datetime import datetime, date, time
import math

precio = Precio(100)


estadias = [
    Estadia(date.today(), "ABC123", "EN_CURSO", time(8, 30)),
    Estadia(date.today(), "ASD321", "FINALIZADA", time(8, 30), time(14, 30), True),

]
