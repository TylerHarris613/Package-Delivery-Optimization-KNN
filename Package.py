
# Class for WGUPS delivery packages


class Package:
    def __init__(self, packageID, deliveryAddress, deliveryCity, deliveryState, deliveryZip, deliveryDeadline,
                 packageWeight, packageStatus):
        # Constructor method that initializes the package object with the provided attributes

        # Package ID
        self.packageID = packageID

        # Delivery address attributes
        self.deliveryAddress = deliveryAddress
        self.deliveryCity = deliveryCity
        self.deliveryState = deliveryState
        self.deliveryZip = deliveryZip

        # Delivery deadline and package weight
        self.deliveryDeadLine = deliveryDeadline
        self.packageWeight = packageWeight

        # Delivery status
        self.packageStatus = packageStatus

        # Departure time and delivery time (initialized as None)
        self.packageDepartureTime = None
        self.packageDeliveryTime = None

    def __str__(self):
        # String representation of the package object
        # Returns a formatted string with package information

        # Format the package details into a multi-line string
        package_details = f"\nPackage ID: {self.packageID} | "
        package_details += f"Delivery Address: {self.deliveryAddress}, "
        package_details += f"{self.deliveryCity}, "
        package_details += f"{self.deliveryState} "
        package_details += f"{self.deliveryZip}"
        package_details += f" | Deadline: {self.deliveryDeadLine}"
        package_details += f" | Weight: {self.packageWeight} kilos"
        package_details += f" | Delivery Time: {self.packageDeliveryTime}"
        package_details += f" | Status: {self.packageStatus}\n"

        return package_details

    def deliveryStatus(self, packageTimedelta):
        # Updates the delivery status for a package based on the given current time

        if packageTimedelta < self.packageDepartureTime:
            self.packageStatus = "At the Hub"
        elif packageTimedelta < self.packageDeliveryTime:
            self.packageStatus = "En route"
        else:
            self.packageStatus = "Delivered"
