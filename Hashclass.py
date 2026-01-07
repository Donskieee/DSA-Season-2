class bdayhash:
    def __init__(self, size=10): #the empty table 
      
        self.size = size
        self.table = [[] for _ in range(self.size)] 

    def hash_core(self, key): #Para dun sa sabi ni art na i convert it the names to module
        total = 0
        for char in key:
            # gets ASCII of a letter
            total += ord(char)
            
        # modulo itself
        return total % self.size

    def add_birthday(self, name, date):
        
        # Calculate the index using your hash function
        index = self.hash_core(name)
        
        #Go to that specific container
        container = self.table[index]
        
        #check if existing name and if yes update it
        for i, (existing_name, existing_date) in enumerate(container):
            if existing_name == name:
                container[i] = (name, date) # Update
                return
        
        #pag wala yung name, I append sya
        container.append((name, date))
        print(f"Stored '{name}' at Index {index}")

    def search_birthday(self, name): #to for the search function
    
        # Calculate the index again 
        index = self.hash_core(name)
        container = self.table[index]
        
        #Look through the container for the name
        for existing_name, existing_date in container:
            if existing_name == name:
                return existing_date
        
        return "Not Found" #stempre ito pag wala duh

