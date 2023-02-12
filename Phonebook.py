from Contact import Contact

class Phonebook:
    
    def __init__(self):
        self.pb = []

    def addressbook(self):

        self.pb.append(Contact("Иванов Иван Иванович", "86756654431", "Москва"))
        self.pb.append(Contact("Котов Олег Петрович", "894567653612", "Самара"))
        self.pb.append(Contact("Петрова Анна Леонтьевна", "89078765543", "Уфа"))

    def show_addressbook(self):
        for i in self.pb:
            print(i.Name + " " + i.Phone + " " + i.City)

    def add_Contact(self):
         n = input("Input name:  ")
         p = input("Input phone:  ")
         c = input("Input city:  ")
         self.pb.append(Contact(n, p, c))        
    
    # def set_name(self, name):
    #     self.Name = name 
    
    # def set_phone(self, phone):
    #     self.Phone = phone 
    
    # def set_city(self, city):
    #     self.City = city 