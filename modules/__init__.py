from . import ryanair
from . import aerlingus
def getAll(date, origin, destination, flexible):
    flights = []
    flights = flights + ryanair.get(date,origin,destination, flexible)
    flights = flights + aerlingus.get(date,origin,destination, flexible)
    return flights