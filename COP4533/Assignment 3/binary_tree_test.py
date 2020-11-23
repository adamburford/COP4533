#Adam Burford
#COP4533
#Section 3594

from binary_tree_string_list import BinaryTreeStringList
from string import ascii_lowercase, ascii_uppercase
from timeit import repeat
from random import choices, randint, randrange
from statistics import mean

def main():

    my_list = []

    for y in (''.join(choices(ascii_uppercase + ascii_lowercase, k = 3)) for _ in range(20)): my_list.append(y)

    my_tree = BinaryTreeStringList()

    for item in my_list:
        my_tree.add(item)

    print("Binary Tree Search Test")

    print("\n\nTimeIt Sort Results\n--------------------------------------------------------------------------------")

    times = repeat("for item in my_list: my_tree.find(item)", globals={"my_list": my_list, "my_tree": my_tree}, number = 1000000, repeat = 5)
    
    print("1,000,000 runs of 20 searches for random string in tree:\n")   
    i = 1
    for time in times: print("Run " + str(i) + ": Total: " + "{0:0.8f}".format(time) + " Per Search: " + "{0:0.8f}".format(time / 20)); i += 1

    print("\n")

if __name__ == "__main__":
	main()