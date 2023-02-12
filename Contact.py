
class Contact:   
    def __init__(self, name, phone, city):
        self.Name = name
        self.Phone = phone
        self.City = city

    def __str__(self):
        return f"Имя: {self.Name}  Телефон: {self.Phone}  Город: {self.City}"

    def get_name(self):
        return self.Name
    
    def get_phone(self):
        return self.Phone 
    
    def get_city(self):
        return self.City    

            
