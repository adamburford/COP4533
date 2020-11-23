#Adam Burford
#COP4533
#Section 3594

from bubble_string_list import BubbleStringList
from string import ascii_lowercase, ascii_uppercase
from timeit import repeat
from random import choices, randint, randrange
from statistics import mean

def main():

    print("BubbleStringList Test")

    print("\n\nTimeIt Sort Results\n--------------------------------------------------------------------------------")

    times = repeat("my_list.sort()", "from string import ascii_lowercase, ascii_uppercase;from bubble_string_list import BubbleStringList;from random import choices;\nmy_list = BubbleStringList();\nfor y in (''.join(choices(ascii_uppercase + ascii_lowercase, k = 3)) for _ in range(100)): my_list.add(y)", number=1, repeat=100000)

    print("100,000 sorts of 100 random strings:\n")
    print("Total Time: " + str(sum(times)) + "\n")
    print("Average Time: " + "{0:0.8f}".format(mean(times)))

    print("\n")

if __name__ == "__main__":
	main()
