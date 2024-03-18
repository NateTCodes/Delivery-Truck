# Nathan Turner
# 011102290

import csv
from datetime import time
from Hashtable import HashTable
from Trucks import Trucks
from Packages import Packages

# The program runs in a space-time complexity of O(n) and O(n^2)
# Calls table from Hashtable.py
Hash = HashTable()

package_list = list()


# Space-time complexity of O(n)
# functions to create instances of packages using csv file
def open_package(file):
    with open(file) as package_details:
        # open and read csv file
        package_info = csv.reader(package_details, delimiter=',')
        next(package_info)
        # assign each column to a variable
        for packages in package_info:
            packageId = int(packages[0])
            package_address = packages[1]
            package_city = packages[2]
            package_state = packages[3]
            package_zipcode = packages[4]
            package_deadline = packages[5]
            package_mass = packages[6]
            package_notes = packages[7]
            package_stat = "At Hub"
            package_time = None
            # create package object
            package_info = Packages(packageId, package_address, package_city, package_state, package_zipcode,
                                    package_deadline, package_mass, package_notes, package_stat, package_time)
            Hash.insert(packageId, package_info)
            package_list.append(packages)  # Adds the data to the list


distance_list = list()


# Space-time complexity of O(n)
def open_distance(file):
    # Read and open csv file
    with open(file) as distance_info:
        distance_info = csv.reader(distance_info, delimiter=',')
        next(distance_info)
        # iterates and adds distance to list
        for dist in distance_info:
            distance_list.append(dist)


address_list = list()


# Space-time complexity of O(n)
def open_address(file):
    # Read and open csv file
    with open(file) as distanceInfo:
        address_info = csv.reader(distanceInfo, delimiter=',')
        next(address_info)
        # iterates through and adds address to list
        for address in address_info:
            address_list.append(address)


# load the files
open_package('Package.csv')
open_distance('Distance.csv')
open_address('Address.csv')


# function to retrieve address ID through package ID
# Space-time complexity of O(1) and O(n)
def address_id(package_id):
    address_returned = None
    # iterate through list with indices to find the address
    for index, package in enumerate(package_list):
        if package_id == index + 1:
            address_returned = package[1]
    # iterate through addresses to find the ID
    for address in address_list:
        if address_returned == address[2]:
            return int(address[0])


# Space-time complexity of O(1)
# function to return distances between two packages
def distance(package_1, package_2):
    return float(distance_list[package_1][package_2])


# Space-time complexity of O(n) and O(n^2)
def algorithm(truck):
    new_route = []
    route = []
    # iterates through to add packages to truck list
    for package in truck.package:
        route.append(package.package_id)
    # sets initial distance to float infinity
    initial_distance = float('inf')
    next_package = None
    # iterate through routes
    for package in route:
        # use distance function to find distance from initial point
        distances = distance(0, address_id(package))
        # update initial distance and current package if condition is true
        if distances < initial_distance:
            initial_distance = distances
            next_package = package
    # add the package and remove from route list
    new_route.append(next_package)
    route.remove(next_package)

    # loop condition until there are no packages in route
    while len(route) > 0:
        nearest_distance = float('inf')
        # iterate through routes and update ID 9
        for package in route:
            # uses distance function to calculate last package and current package distance
            distances = distance(address_id(new_route[-1]), address_id(package))
            # condition to update distance and package if true
            if distances < nearest_distance:
                nearest_distance = distances
                next_package = package
        # add and remove from respective lists
        new_route.append(next_package)
        route.remove(next_package)
    return new_route

# creating class instances
truck_1 = Trucks(1, 0, 0, set())
truck_2 = Trucks(2, 0, 0, set())
truck_3 = Trucks(3, 0, 0, set())

# assigns packages to trucks based on ID manually
truck1_pack_id = [14, 15, 16, 34, 20, 21, 13, 39, 4, 40, 19, 27, 35, 12, 23, 11]
# iterates through and adds the package to truck
for package_id in truck1_pack_id:
    truck_1.add(Hash.search(package_id))
truck1_route = algorithm(truck_1)
truck2_pack_id = [6, 31, 32, 25, 26, 3, 18, 36, 38, 28, 9, 10, 2, 33, 17, 22]
for package_id in truck2_pack_id:
    truck_2.add(Hash.search(package_id))
truck2_route = algorithm(truck_2)
truck3_pack_id = [37, 5, 30, 8, 7, 29, 1, 24]
for package_id in truck3_pack_id:
    truck_3.add(Hash.search(package_id))
truck3_route = algorithm(truck_3)

# Space-time complexity of O(n)
# function to calculate time and mileage
def time_mileage(truck_route):
    mileage_total = 0
    truck_stop = 0
    mileage = []
    # iterates through route and updates the total mileage
    for i in truck_route:
        mileage_total = mileage_total + distance(truck_stop, address_id(i))
        mileage.append(mileage_total)
        truck_stop = address_id(i)
    # handles condition for truck 2 with given start time
    if truck_route == truck2_route:
        initial_time = (9 * 60) + 15
    else:  # time for trucks 1 and 3
        initial_time = 8 * 60
    last_distance = 0
    time_minutes = []
    delivery_time_list = []
    # calculates time per delivery
    for i in mileage:
        time_minutes.append(round((i - last_distance) / 0.3))
        last_distance = i
    # iterates through and adds time to initial in given format
    for i in time_minutes:
        initial_time += i
        hours, minutes = divmod(initial_time, 60)
        delivery_time_list.append(f"{hours:02d}:{minutes:02d}")
    return mileage, delivery_time_list

# applies time_mileage function to each truck route
truck1_tm = time_mileage(truck1_route)
truck2_tm = time_mileage(truck2_route)
truck3_tm = time_mileage(truck3_route)

# Space-time complexity of O(1)
def mileage_calculation():
    # calculates distance of truck 3 return from last stop to start
    truck3_return = distance(12, 0)
    # calculates total mileage and individual mileages
    mileage_total = truck1_tm[0][-1] + truck2_tm[0][-1] + truck3_return + truck3_tm[0][-1]
    truck1_miles = truck1_tm[0][-1]
    truck2_miles = truck2_tm[0][-1]
    truck3_miles = truck3_tm[0][-1] + truck3_return
    return mileage_total, truck1_miles, truck2_miles, truck3_miles

# Space-time complexity of O(n)
# function to update delivery times for packages
def add_delivery(truck_route, mileage):
    times = 0
    for package_id in truck_route:
        Packages.time_update(Hash.search(package_id), mileage[1][times])
        times = times + 1

# uses function and applies it to each truck
add_delivery(truck1_route, truck1_tm)
add_delivery(truck2_route, truck2_tm)
add_delivery(truck3_route, truck3_tm)

# Space-time complexity of O(1)
# function to view individual package status
def individual_package(package_input, time_input):
    # delivery time of packages from table
    package_delivery = time.fromisoformat(Hash.search(package_input).time)
    truck1_3_depart = time(8, 0)
    truck2_depart = time(9, 15)
    # Updated code for Part C
    if package_input == 9 and time_input >= time(10, 20):
        Packages.address_update(Hash.search(9), "410 S State St")
    # condition to check package assignment
    if package_input in truck1_pack_id or package_input in truck3_pack_id:
        # checks to see if time is before the departure of truck 1 and 3
        if time_input < truck1_3_depart:
            # updates status
            Packages.status_update(Hash.search(package_input), "At Hub")
        else:
            if package_delivery > time_input:
                Packages.status_update(Hash.search(package_input), "in route")
            else:
                Packages.status_update(Hash.search(package_input), "Delivered")
    else:
        # truck 2 condition to update status
        if time_input < truck2_depart:
            Packages.status_update(Hash.search(package_input), "At Hub")
        else:
            if package_delivery > time_input:
                Packages.status_update(Hash.search(package_input), "in route")
            else:
                Packages.status_update(Hash.search(package_input), "Delivered")
    # if there is no delivered package then time is set to Null
    if Hash.search(package_input).status != "Delivered":
        Packages.time_update(Hash.search(package_input), "Null")

    print("------------------------------------")
    print("PackageID, Address, City, State, Zipcode, Delivery Deadline, Mass, Additional Information, Status, Time")
    print(Hash.search(package_input))

# Space-time complexity of O(n)
# function to check status of all packages based on a time
def package_status(time_input):
    print("------------------------------------")
    print("PackageID, Address, City, State, Zipcode, Delivery Deadline, Mass, Additional Information, Status, Time")
    truck1_3_depart = time(8, 0)
    truck2_depart = time(9, 15)
    # iterate through the range
    for package_id in range(1, 41):
        # get package delivery time from hash table
        package_delivery = time.fromisoformat(Hash.search(package_id).time)
        # Updated code for Part C
        if package_id == 9 and time_input >= time(10, 20):
            Packages.address_update(Hash.search(9), "410 S State St")
        # condition to check where the package is located and updating status
        if package_id in truck1_pack_id or package_id in truck3_pack_id:
            if time_input < truck1_3_depart:
                Packages.status_update(Hash.search(package_id), "At Hub")
            else:
                if package_delivery > time_input:
                    Packages.status_update(Hash.search(package_id), "in route")
                else:
                    Packages.status_update(Hash.search(package_id), "Delivered")
        else:
            if time_input < truck2_depart:
                Packages.status_update(Hash.search(package_id), "At Hub")
            else:
                if package_delivery > time_input:
                    Packages.status_update(Hash.search(package_id), "in route")
                else:
                    Packages.status_update(Hash.search(package_id), "Delivered")

        if Hash.search(package_id).status != "Delivered":
            Packages.time_update(Hash.search(package_id), "Null")

        print(Hash.search(package_id))

# display menu of program and returns function based on input
def display():
    print("------------------------------------")
    print("Welcome!: Please enter an option between 1-4")
    print("------------------------------------")
    print("1. View the total mileage and status of all packages")
    print("2. Individual package status")
    print("3. All packages in route status")
    print("4. Exit, Thank you! ")
    choice = input("Please enter an option: ")
    if choice == "1":
        choice1()
    elif choice == "2":
        choice2()
    elif choice == "3":
        choice3()
    else:
        choice4()

# total mileage and status display
def choice1():
    print("---------------------------------------")
    print("Truck 1 has traveled " + str(round(mileage_calculation()[1], 1)) + " miles.")
    print("Truck 2 has traveled " + str(round(mileage_calculation()[2], 1)) + " miles.")
    print("Truck 3 has traveled " + str(round(mileage_calculation()[3], 1)) + " miles.")
    print("The mileage to deliver all packages for WGUPS was " + str(round(mileage_calculation()[0], 1)) + " miles.")
    print("---------------------------------------")
    print("View the packages below:")
    print("PackageID, Address, City, State, Zipcode, Delivery Deadline, Mass, Additional Information, Status, Time")
    for package_id in range(1, 41):
        Packages.status_update(Hash.search(package_id), "Delivered")
        print(Hash.search(package_id))


def choice2():
    print("---------------------------------------")
    choice_package = ""
    time_input = ""
    # takes input of packageID
    while choice_package == "":
        try:
            choice_id = input("Enter package ID: ")
            choice_package = int(choice_id)
        except ValueError:
            print("Invalid input, please enter another ID")
    # time input
    while time_input == "":
        try:
            choice_time = input("Please enter a time in 'HH:MM': ")
            hours, minutes = map(int, choice_time.split(":"))
            time_input = time(hours, minutes)
        except ValueError:
            print("Invalid input, please enter another time.")
    # function call with inputs
    individual_package(choice_package, time_input)


def choice3():
    print("---------------------------------------")
    time_input = ""
    while time_input == "":
        try:
            choice_time = input("Please enter a time in 'HH:MM': ")
            hours, minutes = map(int, choice_time.split(":"))
            time_input = time(hours, minutes)
        except ValueError:
            print("Invalid input, please enter another time.")

    package_status(time_input)


def choice4():
    print("---------------------------------------")
    print("Thank you for using WGUPS!")


display()
