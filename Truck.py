# Class for WGUPS Delivery Trucks
class Truck:
    def __init__(self, maxLoad, currentLoad, packagesOnBoard, departTime, truckSpeed, milesDriven, currentAddress):
        # Initialize the Truck object with provided attributes
        self.maxLoad = maxLoad                 # Maximum load capacity of the truck
        self.currentLoad = currentLoad         # Current load of the truck
        # Packages on board the truck
        self.packagesOnBoard = packagesOnBoard
        self.departTime = departTime           # Departure time of the truck
        # Current time of the truck (initialized with departure time)
        self.currentTime = departTime
        self.truckSpeed = truckSpeed           # Speed of the truck
        self.milesDriven = milesDriven         # Miles driven by the truck
        self.currentAddress = currentAddress   # Current address of the truck

    def __str__(self):
        # Return a string representation of the Truck object
        return f"Max Load: {self.maxLoad}, Current Load: {self.currentLoad}, Packages On Board: {self.packagesOnBoard}," \
               f"Departure Time: {self.departTime}, Current Time: {self.currentTime}, Truck Speed: {self.truckSpeed}," \
               f" Miles Driven: {self.milesDriven}, Current Address: {self.currentAddress}"
