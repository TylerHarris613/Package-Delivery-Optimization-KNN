# Tyler Harris | Student ID: #010983966

import datetime
import csv
from builtins import ValueError

from HashMap import InitiateHashMap
from Package import Package
import Truck
import dataManipulation
from truckOperations import truckOperations

# Instantiate hash map
WGUPS_hashMap = InitiateHashMap()


# Load package data from Package_File.csv, store in WGUPS Hash Map
truckOperations.loadAndStorePackages(
    "WGUPS_Files/packageDetails.csv", WGUPS_hashMap)


# Create objects for the WGUPS Delivery Trucks

# Object for WGUPS Delivery Truck #1
# (maxLoad, currentLoad, packagesOnBoard, departTime, truckSpeed, milesDriven, currentAddress)
# Truck leaves at 8:00 AM, earliest time a driver can leave the hub
deliveryTruck1 = Truck.Truck(16, None, [1, 13, 14, 15, 16, 19, 20, 29, 30, 31, 34, 37, 26], datetime.timedelta(
    hours=8, minutes=0, seconds=0), 18, 0.0, "4001 South 700 East")

# Object for WGUPS Delivery Truck #2
# (maxLoad, currentLoad, packagesOnBoard, departTime, truckSpeed, milesDriven, currentAddress)
# Truck leaves at 10:20 AM to account for package ID #9 which had wrong address listed
deliveryTruck2 = Truck.Truck(16, None, [18, 36, 38, 9, 22, 17, 12, 3, 8, 35, 39, 10, 11, 24, 27, 33], datetime.timedelta(
    hours=10, minutes=20), 18, 0.0, "4001 South 700 East")

# Object for WGUPS Delivery Truck #3
# (maxLoad, currentLoad, packagesOnBoard, departTime, truckSpeed, milesDriven, currentAddress)
# Truck leaves hub at 9:05 AM to account for 'delayed on flight' packages
deliveryTruck3 = Truck.Truck(16, None, [6, 25, 28, 32, 21, 40, 2, 4, 5, 7, 23], datetime.timedelta(
    hours=9, minutes=5), 18, 0.0, "4001 South 700 East")


# Load trucks 1 and 2 with packages and initiate delivery
truckOperations.loadAndDeliverPackages(deliveryTruck1, WGUPS_hashMap)
truckOperations.loadAndDeliverPackages(deliveryTruck3, WGUPS_hashMap)
# Set truck 3's departure time to follow the finishing time of the quicker of trucks 1 and 2
deliveryTruck2.departTime = max(datetime.timedelta(hours=10, minutes=20), min(
    deliveryTruck1.currentTime, deliveryTruck3.currentTime))
# Load truck 3 with packages and initiate delivery
truckOperations.loadAndDeliverPackages(deliveryTruck2, WGUPS_hashMap)


# User Interface, with input validation for user input
class Main:
    print("Western Governors University Parcel Service User Interface\n")
    # Calculate the total mileage for all 3 trucks
    totalMilesDriven = deliveryTruck1.milesDriven + \
        deliveryTruck2.milesDriven + deliveryTruck3.milesDriven
    # Print the total mileage traveled by all 3 delivery trucks
    print(
        f"Total mileage traveled by all 3 delivery trucks is {totalMilesDriven} miles\n")

    validTimeFormat = False

    while not validTimeFormat:
        # Prompt the user to enter a time in the correct format or 'q' to quit
        userTime = input(
            "To see further details, input the time of day for which you want to see package statuses. Input the time in the HH:MM:SS format. Example: 11:30:00 (or 'q' to quit)\n")

        if userTime.lower() == 'q':
            exit()

        try:
            (userHour, userMinute, userSecond) = userTime.split(":")
            packageTimedelta = datetime.timedelta(
                hours=int(userHour), minutes=int(userMinute), seconds=int(userSecond))
            validTimeFormat = True
        except ValueError:
            print(
                "Invalid time format. Please enter the time in HH:MM:SS format or 'q' to quit.")
    (userHour, userMinute, userSecond) = userTime.split(":")
    packageTimedelta = datetime.timedelta(
        hours=int(userHour), minutes=int(userMinute), seconds=int(userSecond))
    # Prompt the user to choose between viewing all packages or an individual package
    userPackage = input(
        "To see a detailed breakdown for all packages, input 'ALL'. To see a detailed breakdown for a single package, input 'ONE'\n")

    while True:
        if userPackage.upper() == "ONE":
            try:
                # Prompt the user to enter a package ID to see its breakdown
                userPackageID = input(
                    "Enter the package ID of the package you want a breakdown for. Example: If you want to see package #9, enter '9'\n")
                packageID = int(userPackageID)
                if 1 <= packageID <= 40:
                    package = WGUPS_hashMap.lookup(packageID)
                    package.deliveryStatus(packageTimedelta)
                    print(str(package))
                    break
                else:
                    print("Invalid package ID. Please enter a number between 1 and 40.")
            except ValueError:
                print("Invalid input. Please enter a valid package ID.")
        elif userPackage.upper() == "ALL":
            try:
                for packageID in range(1, 41):
                    package = WGUPS_hashMap.lookup(packageID)
                    package.deliveryStatus(packageTimedelta)
                    print(str(package))
                break
            except ValueError:
                print("Invalid input. Application will now exit")
                exit()
        else:
            print("Invalid input. Please enter 'ALL' or 'ONE'.")
            userPackage = input(
                "To see a detailed breakdown for all packages, input 'ALL'. To see a detailed breakdown for a single package, input 'ONE'\n")
