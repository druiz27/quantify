class HashMap:
    def __init__(self, initial_size):
        self.size = initial_size
        self.map = [[] for _ in range(self.size)]   # initializes HashMap object by creating a list of empty lists

    def _hash(self, key):
        return hash(key) % self.size
        # computes hash value for a given key using hash() function & modulus to get the index within the map

    def insert(self, key, value):
        hashed_key = self._hash(key)    # calculates hashed key to locate bucked based on provided key
        bucket = self.map[hashed_key]   # inserts a key value pair into the hashmap
        for pair in bucket:
            if pair[0] == key:  # if key exists in bucket, it will update the value
                pair[1] = value
                return
        bucket.append([key, value])     # appends new key value pair into the bucket

    def delete(self, key):  # removes a key value pair from hashmap based on the provided key
        hashed_key = self._hash(key)    # calculates the hashed key to locate the bucket based on provided key
        bucket = self.map[hashed_key]

        for i, pair in enumerate(bucket):
            if pair[0] == key:
                del bucket[i]       # deletes pair if the key exists
                return

    def get(self, key):     # retrieves the value associated with a specific key from the hashmap
        hashed_key = self._hash(key)    # calculates hashed key to locate bucket based on provided key
        bucket = self.map[hashed_key]

        for pair in bucket:     # searches for that hashed key within the bucket
            if pair[0] == key:  # if the pair is found, it will return the value for that pair
                return pair[1]
        return None     # returns nothing if it is not found

    def search(self, key):  # removes a key value pair from the hash map based on the provided key
        hashed_key = self._hash(key)    # calculates hashed key to located bucket based on provided key
        bucket = self.map[hashed_key]

        for pair in bucket:     # traverses bucket associated with the hashed key
            if pair[0] == key:  # checks if the provided key exists on the hash map
                return True
        return False

    def display(self):      # displays the entire hashmap by iterating through each bucket and printing its contents
        for i, bucket in enumerate(self.map):
            print(f'Bucket {i}: {bucket}')
