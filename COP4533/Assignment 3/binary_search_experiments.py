from binary_string_list import BinaryStringList
from string import ascii_lowercase, ascii_uppercase
from timeit import timeit, repeat
from random import choices, randint, randrange
from sys import maxsize


def main():
    size = 1000000
    my_list = BinaryStringList()
    my_list._BinaryStringList__list = range(size)

    for i in range(size):
        result = my_list.find(my_list[i])
        if result != my_list[i]: print("Failed"); return

    print(my_list.find(1000001))

    #print("Version 1 Average: " + str(operations / size))

    #$print(timeit("for x in range(1000000): my_list.find_v1(my_list[x])", globals={'my_list': my_list}, number = 2))
    #print(timeit("for x in range(1000000): my_list.find_v2(my_list[x])", globals={'my_list': my_list}, number = 2))

    #operations = 0
    #for i in range(size):
    #    result = my_list.find_v2(my_list[i])
    #    if result[0] != my_list[i]: print("Failed"); return

    #    operations += result[1]

    #print("Version 2 Average: " + str(operations / size))


if __name__ == "__main__":
	main()
