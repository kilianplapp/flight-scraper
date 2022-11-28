import flight_scraper
import csv
import requests

def main():
    date = input("Date (YYYY-MM-DD): ")
    origin = input("Origin Airport (XXX): ")
    destination = input("Destination Airport (XXX): ")
    flexible = input("Flexible Days (Y/N): ")

    #basic input validation

    if len(date) != 10:
        print("Incorrect date format, (YYYY-MM-DD)")
        return
    if len(origin) != 3 or len(destination) != 3:
        print("Incorrect origin or destination format, (XXX)")
        return
    if len(flexible) != 1:
        print("Incorrect flexible days format, (Y/N)")
        return

    session = requests.Session()
    session.headers
    flights = flight_scraper.getAll(date, origin, destination, flexible, session)
    with open('output.csv', 'w') as f:
        writer = csv.writer(f)
        for flight in flights:
            writer.writerow([
                flight.origin,
                flight.destination,
                flight.date,
                flight.link,
                flight.flightNumber,
                flight.fares.price,
                flight.id
            ])
    print("Got fares, wrote to CSV.")
main()  