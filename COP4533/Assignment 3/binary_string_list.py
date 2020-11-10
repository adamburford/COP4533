#Adam Burford
#COP4533
#Section 3594

class BinaryStringList():
    """Binary String List"""

    def __init__(self):
        
        self.__list = []

    def __iter__(self):
        return iter(self.__list)

    def __getitem__(self, key):
        return self.__list[key]

    def __setitem__(self, key, value):
        self.__list[key] = value

    def __str__(self):
        return str(self.__list)

    def add(self, value):
        for i in range(len(self.__list)):
            if self.__list[i] > value:
                self.__list.insert(i, value)
                return

        self.__list.append(value)

    def find(self, key):
        left = 0
        right = len(self.__list) - 1

        while (left < right):

            middle = (left + right) >> 1
                
            if (self.__list[middle] < key):
                left = middle + 1
            else:
                right = middle

        if self.__list[left] == key: return key