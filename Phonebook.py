class Phonebook:
    
    def __init__(self, name, phone, city):
        self.Name = name 
        self.Phone = phone 
        self.City = city 
    
    def get_name(self):
        return self.Name
    
    def get_phone(self):
        return self.Phone 
    
    def get_city(self):
        return self.City
    
    def set_name(self, name):
        self.Name = name 
    
    def set_phone(self, phone):
        self.Phone = phone 
    
    def set_city(self, city):
        self.City = city 