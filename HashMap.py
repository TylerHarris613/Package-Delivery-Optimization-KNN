# Class for Hash Map
class InitiateHashMap:
    def __init__(self, list_count=50):
        self.list = []
        for i in range(list_count):
            # Initialize an empty bucket list for each slot
            self.list.append([])

    # Inserts a new key-value pair into the hash map
    # Returns true for a successfuly inserted KV pair
    def insert(self, key, value):
        # Determine the index of the bucket where this item will be placed
        bucketIndex = hash(key) % len(self.list)
        bucketList = self.list[bucketIndex]

        # Modify already existing keys in the bucket
        for pair in bucketList:
            if pair[0] == key:
                pair[1] = value
                return True

        # Insert item at the end of the bucket given a non-existent key
        pair = [key, value]
        bucketList.append(pair)
        return True

    # Looks up an item in the hash map based on the given key
    # Returns the value associated with the found key
    def lookup(self, key):
        bucketIndex = hash(key) % len(self.list)
        bucketList = self.list[bucketIndex]
        for pair in bucketList:
            if key == pair[0]:
                return pair[1]
        return None

    # Removes an item from the hash map based on the given key
    def remove(self, key):

        slotIndex = hash(key) % len(self.list)
        bucket = self.list[slotIndex]

        # Removes key from the hash table if found in bucket
        if key in bucket:
            bucket.remove(key)
