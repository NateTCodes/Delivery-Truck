class Packages:
    # Space-time complexity of O(1)
    def __init__(self, package_id, address, city, state, zipcode, delivery_deadline, mass, info, status, time):
        # Defines each parameter of the class
        self.package_id = package_id
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.delivery_deadline = delivery_deadline
        self.mass = mass
        self.info = info
        self.status = status
        self.time = time

    # Space-time complexity of O(1)
    # function to update the status of the package
    def status_update(self, new_status):
        self.status = new_status

    # Space-time complexity of O(1)
    # function to update the address of the package
    def address_update(self, new_address):
        self.address = new_address

    # Space-time complexity of O(1)
    # function to update the delivery time of the package
    def time_update(self, new_time):
        self.time = new_time

    def __str__(self):
        return f"{self.package_id}, {self.address}, {self.city}, {self.state}, {self.zipcode}, {self.delivery_deadline}, {self.mass}, {self.info}, {self.status}, {self.time}"
        
