import requests
from .models import classes

def get(date, origin, destination, flex):
    flights = []
    try:
        if str(flex).upper() == "Y":
            flex = 2
        else:
            flex=0
        r = requests.get(f"https://www.ryanair.com/api/booking/v4/en-ie/availability?ADT=1&CHD=0&DateIn=&DateOut={date}&Destination={destination}&Disc=0&INF=0&Origin={origin}&TEEN=0&promoCode=&IncludeConnectingFlights=false&FlexDaysBeforeOut={flex}&FlexDaysOut={flex}&FlexDaysBeforeIn={flex}&FlexDaysIn=2&RoundTrip=false&ToUs=AGREED")
        
        if r.status_code != 200:
            return flights
        
        r = r.json()
        
        for dates in r['trips'][0]['dates']:
            for f in dates['flights']:
                
                #no fares available
                try:
                    if len(f['regularFare']['fares']) == 0:continue
                except KeyError: continue
                fare = classes.fare(
                    f['regularFare']['fareKey'],
                    f['regularFare']['fares'][0]['amount'],
                    f['regularFare']['fares'][0]['type']
                )
                flights.append(classes.flight(
                    origin=f['segments'][0]['origin'],
                    destination=f['segments'][0]['destination'],
                    date=f['segments'][0]['time'][0],
                    link=f"https://www.ryanair.com/en/trip/flights/select?adults=1&teens=0&children=0&infants=0&dateOut={date}&dateIn=&isConnectedFlight=false&discount=0&isReturn=false&promoCode=&originIata={origin}&destinationIata={destination}&tpAdults=1&tpTeens=0&tpChildren=0&tpInfants=0&tpStartDate={date}&tpEndDate=&tpDiscount=0&tpPromoCode=&tpOriginIata={origin}&tpDestinationIata={destination}",
                    flightNumber=f['flightNumber'],
                    id=f['flightKey'],
                    fares=fare
                    ))
    except:
        print("Error getting Ryanair")
    return flights