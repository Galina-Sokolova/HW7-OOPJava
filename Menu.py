from Contact import *
from FileManager import FileManager
from Phonebook import *

class Menu:
    run = FileManager() 
    
    def main_menu(): 
        print("1 - Отобразить справочник")
        print("2 - Считать данные из файла")
        print("3 - Записать данные в файл")
        print("4 - Добавить контакт")
        print("..........................")
        print("Выберите действие: ")
        choice = int(input())
        
        # if choice == 1:  
        #     show_addressbook()  
        
        # elif inp == 2:  
        #     FileManager.fileExport(pb)  
        #     print ("Export finish")
        
        # elif inp == 3:
        #     FileManager.fileImport(pb)
        #     print ("Import finish")

        match choice:
            case 1:
                show_addressbook()


            case 2:
                FileManager.fileExport(pb)
                print("Export finish")
            case 3:
                FileManager.fileImport(pb)
            case 4:
                add_Contact()
                show_addressbook()
        return None    