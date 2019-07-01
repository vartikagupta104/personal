import json

class parserJson():
        
    def __init__(self):
        self.data=open("G:\JSON Parser\input.json")
    
    def print_json(self):
        print(self.data.read())

    def get_keys(self):
        pass