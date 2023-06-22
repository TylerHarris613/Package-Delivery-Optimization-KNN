import datetime
import csv

from HashMap import InitiateHashMap
from Package import Package
from dataManipulation import dataManipulation


# Class for the storage and delivery of packages in trucks
class truckOperations:

    def loadAndStorePackages(file_CSV, hashMap):
        # Load and store packages from the CSV file into the hash map
        with open(file_CSV) as package_info:
            packageData = dataManipulation.loadPackageData()
            for package in packageData:
                packageID = int(package[0])
                deliveryAddress = package[1]
                deliveryCity = package[2]
                deliveryState = package[3]
                deliveryZip = package[4]
                deliveryDeadline = package[5]
                packageWeight = package[6]
                deliveryStatus = "At the Hub"

                storedPackage = Package(packageID, deliveryAddress, deliveryCity, deliveryState, deliveryZip,
                                        deliveryDeadline, packageWeight, deliveryStatus)

                # Load and store package data into identified hash map
                hashMap.insert(packageID, storedPackage)

    def loadAndDeliverPackages(truck, hashMap):
        # Load packages onto a truck and initiate the delivery process
        notDeliveredList = []  # Create an empty list to store all packages
        # Add all packages to the notDeliveredList
        for packageID in truck.packagesOnBoard:
            package = hashMap.lookup(packageID)
            notDeliveredList.append(package)

        truck.packagesOnBoard.clear()  # Clear the packages on board the truck

        # Loop through the notDeliveredList, incrementally add packages to the truck until the list is empty
        while len(notDeliveredList) > 0:
            # Initialize a variable to store the current minimum distance
            holdingAddressCalculation = 2000
            # Initialize a variable to hold the package with the minimum distance
            holdingPackageCalculation = None
            # Find the package with the minimum distance to the truck's current address
            for package in notDeliveredList:
                drivingDistance = dataManipulation.spanningDistance(dataManipulation.stringAddress(
                    truck.currentAddress), dataManipulation.stringAddress(package.deliveryAddress))
                if drivingDistance <= holdingAddressCalculation:
                    holdingAddressCalculation = drivingDistance
                    holdingPackageCalculation = package

            # Append the nearest package to the truck's packagesOnBoard list
            truck.packagesOnBoard.append(holdingPackageCalculation.packageID)
            # Remove the package from the notDeliveredList
            notDeliveredList.remove(holdingPackageCalculation)
            # Increment the miles driven by the truck
            truck.milesDriven += holdingAddressCalculation
            # Update the current address of the truck
            truck.currentAddress = holdingPackageCalculation.deliveryAddress
            # Update the current time of the truck
            truck.currentTime += datetime.timedelta(
                hours=holdingAddressCalculation / 18)
            holdingPackageCalculation.packageDeliveryTime = truck.currentTime
            holdingPackageCalculation.packageDepartureTime = truck.departTime
