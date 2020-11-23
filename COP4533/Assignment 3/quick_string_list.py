#Adam Burford
#COP4533
#Section 3594

class QuickStringList():
    """Quick String List"""

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
        __quick_sort__(self.__list, 0 , len(self.__list) - 1)

def __quick_sort__(list, low, high): 

    if low < high: 
  
        pivot = __partition__(list, low, high) 

        __quick_sort__(list, low, pivot - 1) 
        __quick_sort__(list, pivot + 1, high) 


def __partition__(list, low, high): 

    i = low
    pivot = list[high]
  
    for x in range(low , high): 

        if list[x] < pivot: 
          
            t = list[x]
            list[x] = list[i]
            list[i] = t

            i += 1
  
    t = list[high]
    list[high] = list[i]
    list[i] = t

    return i
  
