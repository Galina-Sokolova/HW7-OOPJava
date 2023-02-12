from Phonebook import *

   
pb = []  
pb.append(Phonebook("Иванов Иван Иванович", "88076455535", "Москва"))
pb.append(Phonebook("Васнецов Алексей Петрович", "80879792321", "Пермь"))
pb.append(Phonebook("Волкова Анна Александровна", "89098767765", "Астрахань"))
        
        
    
def show_addressbook():
    for i in pb:
        print (i.get_name(), i.get_phone(), i.get_city())

def add_Contact():
    n = input("Input name:  ")
    p = input("Input phone:  ")
    c = input("Input city:  ")
    pb.append(Phonebook(n, p, c))        
