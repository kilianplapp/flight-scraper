class flight():
    def __init__(self, origin, destination, date, flightNumber, link, id, fares):

        self.origin = origin
        
        self.destination = destination
        
        self.date = date
        
        self.link = link
        
        self.flightNumber = flightNumber

        self.id = id

        self.fares = fares

class fare():
    def __init__(self, fareId, price, type):
        
        self.price = price
        
        self.fareId = fareId,
        
        self.type = type