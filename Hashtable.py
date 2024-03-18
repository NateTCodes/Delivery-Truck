class HashTable:
    # Space-time complexity of O(1)
    def __init__(self, initial_capacity=40):
        self.table = []
        # iterate through the range and append an empty list within it
        for i in range(initial_capacity):
            self.table.append([])

    # Space-time complexity of O(1) and O(n)
    def insert(self, key, value):
        # modulo operator to assign bucket
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]
        # iterate through list to compare keys and update values
        for i in bucket_list:
            if i[0] == key:
                i[1] = value
                return True
        key_value = [key, value]
        bucket_list.append(key_value)
        return True

    # Space-time complexity of O(1) and O(n)
    def search(self, key):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]
        # iterate through list and compare keys to return value
        for i in bucket_list:
            if i[0] == key:
                return i[1]
        return None

    # Space-time complexity of O(1) and O(n)
    def remove(self, key):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]
        # iterate through the list to find a matching key
        for i in bucket_list:
            if i[0] == key:
                bucket_list.remove([i[0], i[1]])

