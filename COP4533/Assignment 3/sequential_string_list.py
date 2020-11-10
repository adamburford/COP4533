#Adam Burford
#COP4533
#Section 3594

class SequentialStringList(object):
    """List of Strings"""
    
    def __init__(self):
        
        self.__list = []

    def __getitem__(self, key):
        return self.__list[key]

    def __setitem__(self, key, value):
        self.__list[key] = value

    def __str__(self):
        return str(self.__list)

    def __iadd__(self, value):
        print(value)
        self.__list += value

    def __add__(self, value):
        self.__list += value

    def add(self, value):
        self.__list.append(value)

    def find(self, key):
        for item in self.__list:
            if item == key:
                return item
