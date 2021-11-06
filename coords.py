import math
import random

def get_distance(lat1, long1, lat2, long2):

    # approximate radius of earth in km
    R = 6373.0

    lat1 = math.radians(lat1)
    long1 = math.radians(long1)
    lat2 = math.radians(lat2)
    long2 = math.radians(long2)

    dlong = long2 - long1
    dlat = lat2 - lat1

    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlong / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    distance = R * c

    return distance



def get_point(lat, long, angle, distance):
    x2 = (math.cos(angle) * distance) + lat
    y2 = (math.sin(angle) * distance) + long
    km_away = get_distance(lat, long, x2, y2)
    return x2, y2, km_away


def degrees(lat, long, distance):
    #input: distance in km
    #output: y so that y = distance/x = degrees away

    angle = 0.79

    divisor = 0.1
    best_divisor = divisor
    for i in range(100000):
        degrees_guess = distance/divisor
        x2, y2, km_away = get_point(lat, long, angle, degrees_guess)
        best_x2, best_y2, best_km_away = get_point(lat, long, angle, distance/best_divisor)

        if abs(km_away - distance) < abs(best_km_away - distance):
            best_divisor = divisor

        divisor += 0.1

    #print(best_km_away)
    return distance/best_divisor
    

def get_coords(lat, long, distance):
    found = False
    distanceDeg = degrees(lat, long, distance)
    while not found:
        angle = random.uniform(0.0, 360)
        distanceDegCopy = random.uniform(0, distanceDeg)

        x2, y2, km_away = get_point(lat, long, angle, distanceDegCopy)

        if get_distance(lat, long, x2, y2) <= distance and get_distance(lat, long, x2, y2) >= 0:
            found = True

    return x2, y2


if __name__ == '__main__':
    dist_list = []
    for i in range(25):
        x, y = get_coords(43, -79, 50)
        dist_list.append(get_distance(43, -79, x, y))
        
    total = 0
    for i in dist_list:
        total += i

    print(total/len(dist_list))
    print(min(dist_list), max(dist_list))

        







    
    
