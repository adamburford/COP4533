#Adam Burford
#COP4533
#Section 3594

from sequential_string_list import SequentialStringList
from string import ascii_lowercase, ascii_uppercase
from timeit import repeat
from random import choices, randrange

def main():
    my_list = SequentialStringList()

    for y in (''.join(choices(ascii_uppercase + ascii_lowercase, k = 3)) for _ in range(20)): my_list.add(y)

    print("BinaryStringList Test\n--------------------------------------------------------------------------------")
    print("Test List:\n" + str(my_list))
    
    print("\n\nIn List Results\n--------------------------------------------------------------------------------")
    in_list_times = repeat("my_list.find(item)", "from random import randrange; item = my_list[randrange(20)]", globals={'my_list': my_list}, repeat=1)
    i = 1
    for time in in_list_times: print("Run " + str(i) + ": " + "{0:0.8f}".format(time)); i += 1



    print("\n\nNot in List Results\n--------------------------------------------------------------------------------")
    not_in_list_times = repeat("my_list.find('not_in_list')", globals={'my_list': my_list}, repeat=1)
    i = 1
    for time in not_in_list_times: print("Run " + str(i) + ": " + "{0:0.8f}".format(time)); i += 1

    print("\n")

if __name__ == "__main__":
	main()