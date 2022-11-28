from . import ryanair
from . import aerlingus
def getAll(date, origin, destination, flexible, session):
    flights = []
    flights = flights + ryanair.get(date,origin,destination, flexible, session)
    flights = flights + aerlingus.get(date,origin,destination, flexible, session)
    return flights