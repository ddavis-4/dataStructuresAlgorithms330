'''
Dylan Davis
3047302
EECS 330
10/30/23
Hash Map
'''

#Implementation of HashMap
class HashMap:
    def __init__(self, size):
        self.size = size 
        self.hash_table = [[] for _ in range(size)] # 

    def _hash_function(self, key):
        return hash(key) % self.size # return index of table

    # A. 1 inserting key value pairs into the hashmap
    def put(self, key, value):
        # first find table index with the hash function above
        table_i = self._hash_function(key)
        # get the bin spot for the item 
        bin = self.hash_table[table_i]

        # check to see if the key exists 
        for i, (k, v) in enumerate(bin):
            # if it already exists place there any way
            if k == key:
                bin[i] = (key, value)
                return

        # if the key is non existant, make it and append the bin list 
        bin.append((key, value))

    # A. 2 get the hash map value 
    def get(self, key):
         #finding the index to table with hash function
        table_i = self._hash_function(key)
        # get the bin
        bin = self.hash_table[table_i]

        # check if a key matches something in the list 
        for k, v in bin:
            # if the key matches, return associated value
            if k == key:
                return v
        # return None if there was not a key found
        return None

    # A. 3 removeing a value from in a HashMap
    def remove(self, key, value):
         # index to table from hash function above
        table_i = self._hash_function(key)
        # get the bin
        bin = self.hash_table[table_i]

        # loop through the bin list
        for i, (k, v) in enumerate(bin):
            # deleting value if pair matches
            if k == key and v == value:
                del bin[i] # delete bin
                return

    # A. 4 Display HaskMap
    def display(self) -> list[list]:
        # loop through map and display bins
        keyList = [] # list of the keys
        for i, bin in enumerate(self.hash_table):
            print(f"Bin #{i}: {bin}")
            keyList.append(list(i) + v for k,v in bin)
        return keyList

# Trip with maximum number of passengers on flight
    def max_passengers_in_flight(self, flight_number):
        passengers = None # initial is None
        trip_id = None # initial is None

        # go through all key,val pairs in all the bins of the hash table
        for bin in self.hash_table:
            for key, val in bin:
                # If the value is in FlightNode, and if key and flight number match
                if isinstance(val, FlightNode) and key == flight_number:
                    # if they match, we consider a new max
                    if passengers is None or val.passengers > passengers: # if node is greater than the old max
                        passengers = val.passengers # change max key
                        trip_id = val.trip_id # set trip ID to the new max

        return passengers, trip_id

class FlightNode:
    def __init__(self, flight_number, trip_id, passengers):
        self.flight_number = flight_number
        self.trip_id = trip_id
        self.passengers = passengers

# Testing...

# Displaying the hash map
my_hash_map = HashMap(7)
0, 1, 4, 9, 16, 25, 36, 49, 64, 81
my_hash_map.put("aaa", 0)
my_hash_map.put("bbb", 1)
my_hash_map.put("ccc", 4)
my_hash_map.put("ddd", 9)
my_hash_map.put("eee", 16)
my_hash_map.put("fff", 25)
my_hash_map.put("ggg", 36)
my_hash_map.put("hhh", 49)
my_hash_map.put("ccc", 64)
my_hash_map.put("ccc", 81)
my_hash_map.display()  

# Retrieve values from hash map 
print("Retrieve values:")
print("aaa:", my_hash_map.get("aaa"))  
print("bbb:", my_hash_map.get("bbb"))
print("ccc:", my_hash_map.get("ccc"))

# Removing a key-value pair from hashmap
my_hash_map.remove("bbb", 1)  

# Display the new hash map
my_hash_map.display() 

#Max Passengers on Trip
my_map = HashMap(11)
# Add flight nodes (flight_number, trip_id, passengers)
my_map.put(16, FlightNode(16, "Trip 1", 300))
my_map.put(16, FlightNode(16, "Trip 2", 700))
my_map.put(29, FlightNode(29, "Trip 1", 800))
my_map.put(29, FlightNode(29, "Trip 2", 250))
my_map.put(36, FlightNode(29, "Trip 3", 500))
my_map.put(36, FlightNode(36, "Trip 1", 500))
my_map.put(36, FlightNode(36, "Trip 2", 340))
my_map.put(36, FlightNode(36, "Trip 3", 900))
my_map.put(36, FlightNode(36, "Trip 4", 400))
my_map.put(49, FlightNode(49, "Trip 1", 250))
my_map.put(49, FlightNode(49, "Trip 2", 550))

max_passengers = my_map.max_passengers_in_flight(49)

if max_passengers is not None:
    print("Largest number of people in flight at once :", max_passengers)
else:
    print("Flight not found in the map")