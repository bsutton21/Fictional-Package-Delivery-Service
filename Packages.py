# Blake Sutton  -- Student ID: 001109490 

from Distances import *
from ReadCSVData import first_truck_status
from ReadCSVData import second_truck_status
from ReadCSVData import third_truck_status
from ReadCSVData import get_hashtable

import datetime

first_delivery = []
second_delivery = []
third_delivery = []
first_truck = []
second_truck = []
third_truck = []
# the times below represent the times that each truck leaves the hub
first_time = '8:00:00'
second_time = '9:05:00'
third_time = '11:00:00'

# Convert string datetime into datetime.timedelta
(h, m, s) = first_time.split(':')
split_first_time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
(h, m, s) = second_time.split(':')
split_second_time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
(h, m, s) = third_time.split(':')
split_third_time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))

# O(N^2 + 2N) = O(N^2)
def run_first_truck():
    # Updates the delivery status of all packages in the first truck when it leaves the station
    i = 0
    # O(N)
    for value in first_truck_status():
        first_truck_status()[i][9] = first_time
        first_delivery.append(first_truck_status()[i])
        i+=1

    # Compares the addresses on the first truck to the main address list and adds the address index to the list
    # O(N^2)
    try:
        first_count = 0
        for j in first_delivery:
            for k in check_address():
                if k[2] == j[2]:
                    first_truck.append(j[0])
                    first_delivery[first_count][1] = k[0]
            first_count += 1
    except IndexError:
        pass

    # Calls the greedy algorithm to sort the packages in the most efficient manner
    calc_short_dist(first_delivery, 1, 0)
    
    # Runs the first truck through the functions in Dystances.py
    # O(N)
    first_truck_dist = 0
    first_truck_count = 0
    for iterate in range(len(first_opt_ind())):
        try:
            # Calculate the distance of each pacakage along the route
            if range(len(first_opt_ind())).index(iterate) == (len(first_opt_ind()) - 1):
                # Calculate the total distance of the truck
                first_truck_dist = check_distance(int(first_opt_ind()[iterate]), 0, first_truck_dist)
                package_delivery = check_first_truck_time(current_distance(int(first_opt_ind()[iterate]), 0))
            else:
                # Calculate the total distance of the truck
                first_truck_dist = check_distance(int(first_opt_ind()[iterate]), int(first_opt_ind()[iterate + 1]), first_truck_dist)
                package_delivery = check_first_truck_time(current_distance(int(first_opt_ind()[iterate]), int(first_opt_ind()[iterate + 1])))
            first_optimized_truck()[first_truck_count][10] = (str(package_delivery))
            get_hashtable().update(int(first_optimized_truck()[first_truck_count][0]), first_delivery)
            first_truck_count += 1
        except IndexError:
            pass
    return first_truck_dist

# O(N^2 + 2N) = O(N^2)
def run_second_truck():
    # Updates the delivery status of all packages in the second truck when it leaves the station
    i = 0
    # O(N)
    for value in second_truck_status():
        second_truck_status()[i][9] = second_time
        second_delivery.append(second_truck_status()[i])
        i+=1

    # Compares the addresses on the second truck to the main address list and adds the address index to the list
    # O(N^2)
    try:
        second_count = 0
        for j in second_delivery:
            for k in check_address():
                if k[2] == j[2]:
                    second_truck.append(j[0])
                    second_delivery[second_count][1] = k[0]
            second_count += 1
    except IndexError:
        pass

    # Calls the greedy algorithm to sort the packages in the most efficient manner
    calc_short_dist(second_delivery, 2, 0)
    
    # Same as with the first truck
    # Runs the second truck through the functions in Dystances.py
    # O(N)
    second_truck_dist = 0
    second_truck_count = 0
    for iterate in range(len(second_opt_ind())):
        try:
            # Calculate the distance of each pacakage along the route
            if range(len(second_opt_ind())).index(iterate) == (len(second_opt_ind()) - 1):
                # Calculate the total distance of the truck
                second_truck_dist = check_distance(int(second_opt_ind()[iterate]), 0, second_truck_dist)
                package_delivery = check_second_truck_time(current_distance(int(second_opt_ind()[iterate]), 0))
            else:
                # Calculate the total distance of the truck
                second_truck_dist = check_distance(int(second_opt_ind()[iterate]), int(second_opt_ind()[iterate + 1]), second_truck_dist)
                package_delivery = check_second_truck_time(current_distance(int(second_opt_ind()[iterate]), int(second_opt_ind()[iterate + 1])))
            second_optimized_truck()[second_truck_count][10] = (str(package_delivery))
            get_hashtable().update(int(second_optimized_truck()[second_truck_count][0]), second_delivery)
            second_truck_count += 1
        except IndexError:
            pass
    return second_truck_dist

# O(N^2 + 2N) = O(N^2)
def run_third_truck():
    # Updates the delivery status of all packages in the third truck when it leaves the station
    i = 0
    # O(N)
    for value in third_truck_status():
        third_truck_status()[i][9] = third_time
        third_delivery.append(third_truck_status()[i])
        i+=1

    # Compares the addresses on the third truck to the main address list and adds the address index to the list
    # O(N^2)
    try:
        third_count = 0
        for j in third_delivery:
            for k in check_address():
                if k[2] == j[2]:
                    third_truck.append(j[0])
                    third_delivery[third_count][1] = k[0]
            third_count += 1
    except IndexError:
        pass

    # Calls the greedy algorithm to sort the packages in the most efficient manner
    calc_short_dist(third_delivery, 3, 0)

    # Same as with the first two trucks
    # Runs the third truck through the functions in Dystances.py
    # O(N)
    third_truck_dist = 0  
    third_truck_count = 0
    for iterate in range(len(third_opt_ind())):
        try:
            # Calculate the distance of each pacakage along the route
            if range(len(third_opt_ind())).index(iterate) == (len(third_opt_ind()) - 1):
                # Calculate the total distance of the truck
                third_truck_dist = check_distance(int(third_opt_ind()[iterate]), 0, third_truck_dist)
                package_delivery = check_third_truck_time(current_distance(int(third_opt_ind()[iterate]), 0))
            else:
                # Calculate the total distance of the truck
                third_truck_dist = check_distance(int(third_opt_ind()[iterate]), int(third_opt_ind()[iterate + 1]), third_truck_dist)
                package_delivery = check_third_truck_time(current_distance(int(third_opt_ind()[iterate]), int(third_opt_ind()[iterate + 1])))
            third_optimized_truck()[third_truck_count][10] = (str(package_delivery))
            get_hashtable().update(int(third_optimized_truck()[third_truck_count][0]), third_delivery)
            third_truck_count += 1
        except IndexError:
            pass
    return third_truck_dist

# Calculates the total distance traveled by all three trucks
# O(1)
def total_distance():
    # Do I need to define the above trucks in functions and call them here?
    first_truck_dist = run_first_truck()
    second_truck_dist = run_second_truck()
    third_truck_dist = run_third_truck()
    total_distance = first_truck_dist + second_truck_dist + third_truck_dist
    return total_distance