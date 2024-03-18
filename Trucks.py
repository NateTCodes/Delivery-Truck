class Trucks:
    # Space-Time complexity of O(1)
    def __init__(self, id, location, mileage, package):
        # Assigns each variable
        self.id = id
        self.location = location
        self.mileage = mileage

        self.package = package

    # Space-Time complexity of O(1)
    def add(self, packageID):
        self.package.add(packageID)

    def __str__(self):
        return f"{self.id}, {self.package}, {self.location}, {self.mileage}"
