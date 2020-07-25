"""
Please note: 
    first time I use python in my life,
    i have to another 4 projects this weekend so I don't have time to learn the best practise
    to write a good clean code.
    I try to write a readable code. 

Run it:
intall haversine: pip install haversine
"""


import haversine as hs

locations = [
    {'id': 1000, 'zip_code': '37069', 'lat': 45.35, 'lng': 10.84},
    {'id': 1001, 'zip_code': '37121', 'lat': 45.44, 'lng': 10.99},
    {'id': 1001, 'zip_code': '37129', 'lat': 45.44, 'lng': 11.00},
    {'id': 1001, 'zip_code': '37133', 'lat': 45.43, 'lng': 11.02},
]

shoppers = [
    {'id': 'S1', 'lat': 45.46, 'lng': 11.03, 'enabled': False},
    {'id': 'S1', 'lat': 45.46, 'lng': 11.03, 'enabled': True},
    {'id': 'S2', 'lat': 45.46, 'lng': 10.12, 'enabled': True},
    {'id': 'S3', 'lat': 45.34, 'lng': 10.81, 'enabled': True},
    {'id': 'S4', 'lat': 45.76, 'lng': 10.57, 'enabled': True},
    {'id': 'S5', 'lat': 45.34, 'lng': 10.63, 'enabled': True},
    {'id': 'S6', 'lat': 45.42, 'lng': 10.81, 'enabled': True},
    {'id': 'S7', 'lat': 45.34, 'lng': 10.94, 'enabled': True},
]


def lessThan10Km(shopperLocation, location):
    if(hs.haversine(shopperLocation, location) < 10):
        return True
    else:
        return False


def coverage(shopCovered, totalShops):
    return shopCovered * 100 / totalShops


def isEnabled(shopper):
    return shopper['enabled']


def getCoordinates(element):
    return (element['lat'], element['lng'])


def locationsCovered(shopper, locations):
    count = 0
    for l in locations:
        if(lessThan10Km(getCoordinates(shopper), getCoordinates(l))):
            count += 1
    return count


def addShopperCoverage(shopper, locations, result):
    if(isEnabled(shopper)):
        locationsCoveredCount = locationsCovered(shopper, locations)
        result.append(
            {'shopper_id': shopper['id'],
             'coverage': coverage(locationsCoveredCount, len(locations))
            }
        )


def shoppersLocationsCovered(shoppers, locations):
    result = []
    for shopper in shoppers:
        addShopperCoverage(shopper, locations, result)
    return sorted(result, key=lambda k: k['coverage'], reverse=True)


for shopper_coverage in shoppersLocationsCovered(shoppers, locations):
    print(shopper_coverage)
