import csv
from collections import Iterable

import requests as requests


def ito_gov() -> Iterable[str]:
    ips = set()
    with open('resources/ito_gov.html', 'r') as f:
        lines = f.readlines()
        for line in lines:
            if '<td>' in line:
                ips.add(line.split('<td>')[2].split('</td>')[0])

    return ips


def ip2location() -> Iterable[str]:
    with open('resources/ip2location.csv', 'r') as f:
        csv_reader = csv.reader(f, delimiter=',')
        return set(line[0] for line in csv_reader if 'IR' in line[1])


def geo_lite2() -> Iterable[str]:
    with open('resources/GeoLite2-Country-Locations-en.csv', 'r') as f:
        csv_reader = csv.reader(f, delimiter=',')
        for line in csv_reader:
            if line[4] == 'IR':
                iran_code = line[0]
                break

    with open('resources/GeoLite2-Country-Blocks-IPv4.csv', 'r') as f:
        csv_reader = csv.reader(f, delimiter=',')
        return set(line[0] for line in csv_reader if line[2] == iran_code)


def get_arvan() -> Iterable[str]:
    request = requests.get('https://www.arvancloud.com/en/ips.txt')
    return request.text.splitlines()
