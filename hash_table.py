import json
import os
import shutil # Added to handle the auto-restore copying

class BirthdayHash:
    def __init__(self, size=366): # Size 366 covers all possible days roughly
        self.size = size
        # The table is a list of buckets.
        # Each bucket will store tuples: (Date_Key, [List_of_Names])
        self.table = [[] for _ in range(self.size)]
        self.filename = "birthdays.json"
        self.backup_filename = "backup_birthdays.json" # Define backup name
        self.load_data()  # Load data when program starts

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
                self.save_data() # SAVE!
                return
        
        # If the date key is new in this bucket, create a new entry
        # Structure: (Date, [List containing the name])
        bucket.append((date, [name]))
        print(f"Created new entry for {date} with {name}.")
        self.save_data() # SAVE!

    def delete_birthday(self, name_to_delete):
        """Removes a name from the hash table."""
        found = False
        for bucket in self.table:
            for i, (date, names_list) in enumerate(bucket):
                if name_to_delete in names_list:
                    names_list.remove(name_to_delete)
                    if not names_list: # If list is empty, remove the tuple
                        del bucket[i]
                    found = True
        
        if found:
            self.save_data() # SAVE!
            return True
        return False

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
        return found_matches if found_matches else []

    def get_all_birthdays(self):
        """Returns a list of dictionaries for the calendar/checker."""
        all_data = []
        for bucket in self.table:
            for date, names_list in bucket:
                # Assuming date format is "Month-Day" (e.g., "1-11")
                try:
                    m, d = map(int, date.split('-'))
                    for name in names_list:
                        all_data.append({"name": name, "month": m, "day": d})
                except ValueError:
                    continue
        return all_data

    def save_data(self):
        """Saves current table to JSON for the background checker."""
        data_to_save = self.get_all_birthdays()
        with open(self.filename, 'w') as f:
            json.dump(data_to_save, f, indent=4)

    def load_data(self):
        if not os.path.exists(self.filename):
            # If main file missing, checks for the backup.
            if os.path.exists(self.backup_filename):
                print("⚠️ Main database missing! Restoring from backup...")
                try:
                    shutil.copy(self.backup_filename, self.filename)
                    print("✅ Data successfully restored.")
                except Exception as e:
                    print(f"❌ Failed to restore backup: {e}")
                    return
            else:
                # No main file AND no backup file
                return 

        try:
            with open(self.filename, 'r') as f:
                data = json.load(f)
                for item in data:
                    # Re-insert without saving to avoid infinite loop
                    date_key = f"{item['month']}-{item['day']}"
                    index = self.hash_core(date_key)
                    bucket = self.table[index]
                    
                    found_date = False
                    for ex_date, names in bucket:
                        if ex_date == date_key:
                            names.append(item['name'])
                            found_date = True
                            break
                    if not found_date:
                        bucket.append((date_key, [item['name']]))
        except:
            pass