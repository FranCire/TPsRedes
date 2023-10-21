import requests
import sys
sys.path.append('TP2')
import save_and_load

COORDS_OLIVOS = '-34.5131817', '-58.5188471'
IPSTACK_ACCESS_KEY = 'c4b7a52cb96588aecd2376cf2b50ce08'
WORKING_DIR = '/workspaces/TPsRedes/TP2/'

def save_coordinates(rtt_files):
    coordinates = {}
    all_ips = []
    for file in rtt_files:
        all_ips += __scrape_ips_from(file)
    for ip in set(all_ips):
        coordinates[ip] = __get_coordinates_from_ip(ip)
    save_and_load.write_object_to_file(coordinates, WORKING_DIR + "geo/coordinates_by_ip.txt")

def __scrape_ips_from(file):
    jumps = save_and_load.read_object_from_file(file)
    ips = []
    for (_, _, ip_from, ip_to, _) in jumps:
        ips += [ip_from, ip_to]
    return ips

def __get_coordinates_from_ip(ip):
    if ip == '0.0.0.0' or ip.startswith('192.168'):
        return COORDS_OLIVOS

    if IPSTACK_ACCESS_KEY == None:
        raise Exception("IP Stack API access key not set")
    request_url = f"http://api.ipstack.com/{ip}?access_key={IPSTACK_ACCESS_KEY}"
    response_json = requests.get(request_url).json()
    return response_json["latitude"], response_json["longitude"]

save_coordinates([WORKING_DIR + filename for filename in [
    'rtt_between_jumps_cam.ac.uk.txt', 
    'rtt_between_jumps_jhu.edu.txt',
    'rtt_between_jumps_uj.ac.za.txt',
    'rtt_between_jumps_www.u-tokyo.ac.jp.txt']
])