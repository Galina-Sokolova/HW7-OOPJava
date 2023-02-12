from Contact import *
from FileManager import FileManager
from Phonebook import *

class Menu:
    def main_menu(): 
        print("1 - Отобразить справочник")
        print("2 - Считать данные из файла")
        print("3 - Записать данные в файл")
        print("4 - Добавить контакт")
        print("..........................")
        print("Выберите действие: ")
        choice = int(input())
        phones = Phonebook()
        phones.addressbook()
        match choice:
            case 1:
                phones.show_addressbook()
            case 2:
                FileManager.fileImport(phones.pb)
            case 3:
                FileManager.fileExport(phones.pb)
                print("Export finish")
            case 4:
                phones.add_Contact()
                phones.show_addressbook()
        return None    