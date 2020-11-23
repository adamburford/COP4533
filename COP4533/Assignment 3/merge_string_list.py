#Adam Burford
#COP4533
#Section 3594

class MergeStringList(object):
    """Merge String List"""

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
        __merge_sort__(self.__list)

def __merge_sort__(list):

    if len(list) > 1:

        middle = len(list) >> 1

        left = list[:middle]
        right = list[middle:]

        __merge_sort__(left)
        __merge_sort__(right)

        __merge__(list, left, right)


def __merge__(list, left, right):

    l = r = i = 0
  
    while l < len(left) and r < len(right):
            
        if left[l] < right[r]:
            list[i] = left[l]
            l += 1
        else:
            list[i] = right[r]
            r += 1

        i += 1
 
    while l < len(left):
        list[i] = left[l]
        i += 1
        l += 1
 
    while r < len(right):
        list[i] = right[r]
        r += 1
        i += 1

