#Adam Burford
#COP4533
#Section 3594

from quick_string_list import QuickStringList
from string import ascii_lowercase, ascii_uppercase
from timeit import repeat
from random import choices, randint, randrange
from statistics import mean

def main():

    #for x in range(1000):

    #    my_list = QuickStringList()

    #    for y in (''.join(choices(ascii_uppercase + ascii_lowercase, k = 3)) for _ in range(10001)): my_list.add(y)

    #    my_list.sort()
    #    test = sorted(my_list._QuickStringList__list)
    #    if my_list._QuickStringList__list != test:
    #        print("Failed")
    #        break

    #    print("Pass: " + str(x))

    #my_list = BubbleStringList()

    #for y in (''.join(choices(ascii_uppercase + ascii_lowercase, k = 3)) for _ in range(1000)): my_list.add(y)

    print("QuickStringList Test")
    #print("Test List: " + str(my_list))
    
    #my_list.sort()
    #print("Sorted List: " + str(my_list))

    print("\n\nTimeIt Sort Results\n--------------------------------------------------------------------------------")

    times = repeat("my_list.sort()", "from string import ascii_lowercase, ascii_uppercase;from quick_string_list import QuickStringList;from random import choices;\nmy_list = QuickStringList();\nfor y in (''.join(choices(ascii_uppercase + ascii_lowercase, k = 3)) for _ in range(100)): my_list.add(y)", number=1, repeat=100000)
    #i = 1
    #for time in in_list_times: print("Run " + str(i) + ": " + "{0:0.8f}".format(time)); i += 1

    print("100,000 sorts of 100 random strings:\n")
    print("Total Time: " + str(sum(times)) + "\n")
    print("Average Time: " + "{0:0.8f}".format(mean(times)))

    print("\n")

if __name__ == "__main__":
	main()