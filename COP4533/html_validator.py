#Adam Burford
#COP4533
#Section 3594

from html.parser import HTMLParser
import timeit
from statistics import mean

class HTMLChecker(HTMLParser):
	#Validates html tags
	#Uses HTMLParser class from python standard library to tokenize the html
	#beacuse I'm too lazy to write a parser myself
	tag_stack = []
	is_valid = True
	count = 0
	def validate_html_file(self, file_name):

		self.tag_stack = []
		self.is_valid = True

		with open(file_name, 'r') as html_file:
			html_string = html_file.read()

		self.feed(html_string)

		return self.is_valid and len(self.tag_stack) == 0

	def handle_starttag(self, tag, attrs):
		self.tag_stack.append(tag)

	def handle_endtag(self, tag):
		if self.tag_stack.pop() != tag:
			self.is_valid = False
		else:
			self.count += 1

def run_test(html_checker, file_name):
	html_checker.validate_html_file(file_name)
	return html_checker.count

def main():
	file_name = input("Enter file name: ")
	hmtl_checker = HTMLChecker()
	
	print("\nValidating HTML tags:")
	if hmtl_checker.validate_html_file(file_name):
		print("Valid HTML")
	else:
		print("Invalid HTML, mismatched opening and closing braces")

	timeit.template = """
def inner(_it, _timer{init}):
    {setup}
    _t0 = _timer()
    for _i in _it:
        retval = {stmt}
    _t1 = _timer()
    return _t1 - _t0, retval
"""

	print("\ntimeit test of html tag validation on ~5KB html file (5 runs):")
	print("-----------------------------------------------------------------")
	times = timeit.repeat(setup = "html_checker = HTMLChecker()", stmt = "run_test(html_checker, 'html_test_valid.txt')", number = 1, repeat = 5, globals=globals())
	
	print("HTML Tags Matched in file (html_test_valid_large.txt): " + str(times[0][1]))
	count = 1
	for time in times:
		print("Run " + str(count) + ": " + str("{0:0.5f}".format(time[0])))
		count += 1
	print("Average: " + str(mean(time[0] for time in times)))

	print("\ntimeit test of html tag validation on ~50KB html file (5 runs):")
	print("-----------------------------------------------------------------")
	times = timeit.repeat(setup = "html_checker = HTMLChecker()", stmt = "run_test(html_checker, 'html_test_valid_large.txt')", number = 1, repeat = 5, globals=globals())
	
	print("HTML Tags Matched in file (html_test_valid_large.txt): " + str(times[0][1]))
	count = 1
	for time in times:
		print("Run " + str(count) + ": " + str("{0:0.5f}".format(time[0])))
		count += 1
	print("Average: " + str(mean(time[0] for time in times)))

	print("\ntimeit test of html tag validation on ~500KB html file (5 runs):")
	print("-----------------------------------------------------------------")
	times = timeit.repeat(setup = "html_checker = HTMLChecker()", stmt = "run_test(html_checker, 'html_test_valid_very_large.txt')", number = 1, repeat = 5, globals=globals())
	
	print("HTML Tags Matched in file (html_test_valid_large.txt): " + str(times[0][1]))
	count = 1
	for time in times:
		print("Run " + str(count) + ": " + str("{0:0.5f}".format(time[0])))
		count += 1
	print("Average: " + str(mean(time[0] for time in times)))



if __name__ == "__main__":
	main()