#Adam Burford
#COP4533
#Section 3594

def recursiveMax(iterable, max_index = 0, current_index = 0):

	if current_index == len(iterable):
		return iterable[max_index]

	if iterable[current_index] > iterable[max_index]:
		return recursiveMax(iterable, current_index, current_index + 1)
	else:
		return recursiveMax(iterable, max_index, current_index + 1)

def main():

	testList = [1,2,3,4,5]
	print(recursiveMax(testList))

	testList = [5,4,3,2,1]
	print(recursiveMax(testList))

	testList = [4, 1, 5, 3, 2]
	print(recursiveMax(testList))

if __name__ == "__main__":
	main()

