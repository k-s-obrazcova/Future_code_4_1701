from datetime import datetime
import pytz


def calculate_individual_flight_time(flight):
    departure_time = datetime.strptime(flight['departure_time'], '%Y-%m-%d %H:%M:%S')
    arrival_time = datetime.strptime(flight['arrival_time'], '%Y-%m-%d %H:%M:%S')

    departure_timezone = pytz.timezone(flight['departure_timezone'])
    arrival_timezone = pytz.timezone(flight['arrival_timezone'])

    departure_time = departure_timezone.localize(departure_time)
    arrival_time = arrival_timezone.localize(arrival_time)

    flight_duration = (arrival_time - departure_time).total_seconds() / 60

    return flight_duration

def calculate_total_and_average_flight_time(flight):
    total_flight_time = 0
    flight_count = 0

    for flight in flights:
        flight_duration = calculate_individual_flight_time(flight)
        print(f"Время полета для рейса {flight['number']} - {flight_duration} минут ")
        total_flight_time += flight_duration
        flight_count += 1

    average_flight_time = total_flight_time / flight_count if flight_count else 0

    return total_flight_time, average_flight_time



flights = [
    {
        'number': 'RT256-02',
        'departure_time': '2024-07-01 08:00:00',
        'arrival_time': '2024-07-01 14:00:00',
        'departure_timezone': 'Europe/Moscow',
        'arrival_timezone': 'Europe/Kaliningrad'
    },
    {
        'number': 'RT220-01',
        'departure_time': '2024-07-05 02:40:00',
        'arrival_time': '2024-07-05 16:50:00',
        'departure_timezone': 'Europe/Moscow',
        'arrival_timezone': 'Asia/Tokyo'
    }
]

print(calculate_individual_flight_time(flights[0]))