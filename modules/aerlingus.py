import requests
from .models import classes

def get(date, origin, destination, flex):
    flights = []
    date = str(date).split('-')
    date = date[2] + "%2F" + date[1] + "%2F" + date[0]
    if str(flex).upper() == "Y":
        
        r = requests.get(f"https://www.aerlingus.com/api/v2/flights/flexible?departureDate={date}&destination={destination}&fare=low&numAdults=1&numChildren=0&numInfants=0&numYouths=0&origin={origin}")
        if r.status_code != 200:
            print("Error getting Aer Lingus flights.")
            return flights
        r = r.json()
        for flight in r['data']['alternativeDates']['outbound']['dates']:
            fare = classes.fare(
                fareId="",
                price=flight['price'],
                type=""
            )
            flights.append(classes.flight(
                origin=origin,
                destination=destination,
                date=flight['date'],
                flightNumber="n/a",
                link="n/a",
                id="n/a",
                fares=fare
            ))
    else:
        r = requests.get(f"https://www.aerlingus.com/api/v2/flights/fixed?departureDate={date}&destination={destination}&fare=low&numAdults=1&numChildren=0&numInfants=0&numYouths=0&origin={origin}")
        
        if r.status_code != 200:
            print("Error getting Aer Lingus flights.")
            return flights
    
        r = r.json()
        if r['data']['journey']['outbound']['flights'] == None:
            print("No flights from Aer Lingus on selected days.")
            return flights
            
        for flight in r['data']['journey']['outbound']['flights']:
            fare = classes.fare(
                type=flight['priceInfo']['fares'][0]['type'],
                fareId=flight['priceInfo']['fares'][0]['basisCodes'][0]['basisCode'],
                price=flight['priceInfo']['fares'][0]['price']
            )
            flights.append(
                classes.flight(
                    origin=flight['trips'][0]['departure']['airportCode'],
                    destination=flight['trips'][0]['arrival']['airportCode'],
                    date=flight['trips'][0]['departure']['date'],
                    flightNumber=flight['trips'][0]['info']['code'],
                    fares=fare,
                    id=flight['trips'][0]['info']['code'],
                    link=""
                )
            )
    return flights