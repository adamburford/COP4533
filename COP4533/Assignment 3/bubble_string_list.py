#Adam Burford
#COP4533
#Section 3594

class BubbleStringList():
    """Bubble String List"""


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

    def __len__(self):
        return len(self.__list)

    def add(self, value):
        self.__list.append(value)
        
    def sort(self):
        max = len(self.__list)

        swapped = True
        while swapped:

            swapped = False
            new_max = 0

            for i in range(1, max):

                if self.__list[i - 1] > self.__list[i]:
                    t = self.__list[i]
                    self.__list[i] = self.__list[i - 1]
                    self.__list[i - 1] = t

                    swapped = True
                    new_max = i

            max = new_max