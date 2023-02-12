import csv
from Phonebook import Phonebook


class FileManager:
    
    def fileExport(pb): 
        with open("export.csv", 'w', encoding="utf-8") as writer: 
            for i in range (0, len(pb)): 
                text = pb[i].get_name() + ';' + pb[i].get_phone() + ';' + pb[i].get_city() 
                writer.write(text)  
                writer.write('\n')  
            writer.flush()  
    
    def fileImport(pb):  
        with open("export.csv", 'r', encoding="utf-8") as reader: 
            for line in reader:
                print(line) 
                    