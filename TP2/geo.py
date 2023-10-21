from math import radians, sin, cos, sqrt, atan2
import requests

IPSTACK_ACCESS_KEY = None

def calculate_distance_between_ips(ip1, ip2):
    lat1, lon1 = get_coordinates_from_ip(ip1)
    lat2, lon2 = get_coordinates_from_ip(ip2)
    return calculate_distance_between_coordinates(lat1, lon1, lat2, lon2)

def calculate_distance_between_coordinates(lat1, lon1, lat2, lon2):
    # Convert latitude and longitude from degrees to radians
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])

    # Haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    # Radius of the Earth in kilometers
    R = 6371.0
    # Calculate the distance
    distance = R * c

    # print(distance)
    return distance

def get_coordinates_from_ip(ip):
    if IPSTACK_ACCESS_KEY == None:
        raise Exception("IP Stack API access key not set")
    request_url = f"http://api.ipstack.com/{ip}?access_key={IPSTACK_ACCESS_KEY}"
    response_json = requests.get(request_url).json()
    return response_json["latitude"], response_json["longitude"]
    