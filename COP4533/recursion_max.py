#Adam Burford
#COP4533
#Section 3594

import timeit
import random
from statistics import mean
import sys

def recursiveMax(iterable, max_index = 0, current_index = 0):

	if current_index == len(iterable):
		return iterable[max_index]

	if iterable[current_index] > iterable[max_index]:
		return recursiveMax(iterable, current_index, current_index + 1)
	else:
		return recursiveMax(iterable, max_index, current_index + 1)

def main():

	timeit.template = """
def inner(_it, _timer{init}):
    {setup}
    _t0 = _timer()
    for _i in _it:
        retval = {stmt}
    _t1 = _timer()
    return _t1 - _t0, retval
"""

	sys_limit = sys.getrecursionlimit
	recursion_limit = 990
	small_recursion_limit = 99

	print("Test Results for recursive max function\n")

	print("Finding max in list of " + str(small_recursion_limit) + " numbers, 10,000 times, 5 runs each")
	print("-------------------------------------")

	print("Recursive function: ")
	times = timeit.repeat(setup = "python_list = []\nfor x in range(" + str(small_recursion_limit)+ "):\n	python_list.append(random.randrange(1,1001))", stmt = "max = recursiveMax(python_list)", number = 10000, repeat = 5, globals=globals())
	count = 1
	for time in times:
		print("Run " + str(count) + ": Time: " + str("{0:0.8f}".format(time[0])) + " Max: " + str(time[1]))
		count += 1
	print("Average: " + str(mean(time[0]for time in times)))

	print("\nPython Library Max() function (for comparison): ")
	times = timeit.repeat(setup = "python_list = []\nfor x in range(" + str(small_recursion_limit)+ "):\n	python_list.append(random.randrange(1,1001))", stmt = "max = recursiveMax(python_list)", number = 10000, repeat = 5, globals=globals())
	count = 1
	for time in times:
		print("Run " + str(count) + ": Time: " + str("{0:0.8f}".format(time[0])) + " Max: " + str(time[1]))
		count += 1
	print("Average: " + str(mean(time[0]for time in times)))

	print("\n\nFinding max in list of " + str(recursion_limit) + " numbers, 10,000 times, 5 runs each")
	print("-------------------------------------")

	print("Recursive function: ")
	times = timeit.repeat(setup = "python_list = []\nfor x in range(" + str(recursion_limit)+ "):\n	python_list.append(random.randrange(1,1001))", stmt = "max = recursiveMax(python_list)", number = 10000, repeat = 5, globals=globals())
	count = 1
	for time in times:
		print("Run " + str(count) + ": Time: " + str("{0:0.8f}".format(time[0])) + " Max: " + str(time[1]))
		count += 1
	print("Average: " + str(mean(time[0]for time in times)))

	print("\nPython Library Max() function (for comparison): ")
	times = timeit.repeat(setup = "python_list = []\nfor x in range(" + str(recursion_limit)+ "):\n	python_list.append(random.randrange(1,1001))", stmt = "max = recursiveMax(python_list)", number = 10000, repeat = 5, globals=globals())
	count = 1
	for time in times:
		print("Run " + str(count) + ": Time: " + str("{0:0.8f}".format(time[0])) + " Max: " + str(time[1]))
		count += 1
	print("Average: " + str(mean(time[0]for time in times)))

	print("\n")
if __name__ == "__main__":
	main()

