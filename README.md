# Package Delivery Optimization Application
## Overview
This Python-based application is designed to assist the Western Governors University Parcel Service (WGUPS) in determining the most efficient delivery routes for their trucks. The program utilizes the Nearest Neighbor algorithm and a custom hashing mechanism to achieve its goal.
## Key Features
- Loading and parsing of package data from CSV files.
- Conversion of delivery address strings to integer address IDs.
- Calculation of distance between two address IDs.
- Creation and management of delivery trucks.
- Loading and delivering of packages in the shortest distance via KNN algorithm
- User interface that provides package status at a specified time.

## Code Structure
### Main Files
- main.py: This file houses the main execution logic of the application, including the creation of truck instances, the loading and delivering of packages, and the user interface for viewing package statuses.
- HashMap.py: Implements the custom Hash Map used for storing package information. The Hash Map uses a bucket hash map with 50 buckets by default. It includes methods to insert a key-value pair, look up a value by key, and remove a key-value pair.
- Package.py: Defines the Package class used in the application.
- Truck.py: Defines the Truck class used in the application.
- dataManipulation.py: Includes functions for loading data from CSV files, converting delivery address strings to integer address IDs, and calculating the distance between two address IDs.
- truckOperations.py: Contains functions for loading package data, loading packages onto trucks, and initiating delivery.
### Classes
- Truck: Represents a delivery truck, with properties such as maximum load, current load, packages on board, departure time, truck speed, miles driven, and current address.
- Package: Represents a package, with properties such as package ID, delivery status, and so on.
- InitiateHashMap: Represents a custom hash map. The hash map uses a bucket hash map with 50 buckets by default. It includes methods to insert a key-value pair, look up a value by key, and remove a key-value pair.
### Important Functions
- loadAndStorePackages: Loads package data from a CSV file and stores it in a Hash Map.
- loadAndDeliverPackages: Loads packages onto a truck and initiates delivery.
- stringAddress: Converts delivery address string to integer address ID.
- spanningDistance: Calculates the distance between two address IDs.
- loadAddressData: Reads data from an Address List CSV and returns the parsed address data.
- loadDistanceData: Reads data from a Distance Matrix CSV and returns the parsed distance data.
- loadPackageData: Reads data from a Package Details CSV and returns the parsed package data.
## How to Run
1. Ensure you have Python 3 installed on your machine.
2. Clone this repository to your local machine.
3. Make sure your CSV files for package data are in the correct format and that the file paths in main.py and dataManipulation.py are set correctly.
4. Run the main.py script.
## Contributions
Contributions, issues and feature requests are welcome.
## License
This project is licensed under the MIT License.
