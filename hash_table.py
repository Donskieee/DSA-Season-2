class BirthdayHash:
    def __init__(self, size=366): # Size 366 covers all possible days roughly
        self.size = size
        # The table is a list of buckets.
        # Each bucket will store tuples: (Date_Key, [List_of_Names])
        self.table = [[] for _ in range(self.size)]

    def hash_core(self, date_key): 
        # We use the built-in hash function on the date string (e.g., "12-25")
        return hash(date_key) % self.size

    def add_birthday(self, name, date):
        index = self.hash_core(date)
        bucket = self.table[index]
        
        # Check if this Date already exists in the bucket
        for i, (existing_date, names_list) in enumerate(bucket):
            if existing_date == date:
                # The date exists! Now check for duplicate name to avoid total redundancy
                if name in names_list:
                    print(f"Error: {name} is already registered for {date}.")
                    return
                # If name is new, append to the list of names for this date
                names_list.append(name)
                print(f"Added {name} to the existing list for {date}.")
                return
        
        # If the date key is new in this bucket, create a new entry
        # Structure: (Date, [List containing the name])
        bucket.append((date, [name]))
        print(f"Created new entry for {date} with {name}.")

    def search_by_date(self, date):
        # fast O(1) search
        index = self.hash_core(date)
        bucket = self.table[index]
        
        for existing_date, names_list in bucket:
            if existing_date == date:
                return names_list # Returns the list of all people born on this date
        return None

    def search_by_name(self, name_to_find):
        # Slower O(N) search, but necessary if Date is the key.
        # We have to look through every bucket.
        found_matches = []
        for bucket in self.table:
            for date, names_list in bucket:
                if name_to_find in names_list:
                    found_matches.append(date)
        return found_matches if found_matches else "Not Found"
