import csv

from HashMap import InitiateHashMap


# Class for parsing data from the WGUPS csv's, and then manipulating that data for distance calculation purposes
class dataManipulation:

    addressCSV = None
    distanceCSV = None

    def stringAddress(deliveryAddress):
        # Helper function to convert delivery address string to integer address ID
        for row in dataManipulation.loadAddressData():
            if deliveryAddress in row[2]:
                return int(row[0])

    def spanningDistance(xValue, yValue):
        # Helper function to calculate the distance between two address IDs
        distanceBetween = dataManipulation.loadDistanceData()[xValue][yValue]
        if distanceBetween == '':
            distanceBetween = dataManipulation.loadDistanceData()[
                yValue][xValue]

        return float(distanceBetween)

    def loadAddressData():
        # Read data from Address List CSV and return the parsed address data
        with open("WGUPS_Files/addressList.csv") as addressFile:
            addressCSV = list(csv.reader(addressFile))
        return addressCSV

    def loadDistanceData():
        # Read data from Distance Matrix CSV and return the parsed distance data
        with open("WGUPS_Files/distanceMatrix.csv") as distanceFile:
            distanceCSV = list(csv.reader(distanceFile))
        return distanceCSV

    def loadPackageData():
        # Read data from Package Details CSV and return the parsed package data
        with open("WGUPS_Files/packageDetails.csv") as packageFile:
            packageCSV = list(csv.reader(packageFile))
        return packageCSV
