#Adam Burford
#COP4533
#Section 3594

from html.parser import HTMLParser


#Use html parser class from python standard library to tokenize the html
#beacuse I'm too lazy to write a parser myself
class HTMLChecker(HTMLParser):
	
	tag_stack = []
	is_valid = True

	def validate_html_file(self, file_name):

		tag_stack = []
		is_valid = True

		file = open(file_name)

		self.feed(file.read())

		if (is_valid and len(tag_stack) == 0):
			return True
		else:
			return False

	def handle_starttag(self, tag, attrs):
		self.tag_stack.push(tag)

	def handle_endtag(self, tag):
		if self.tag_stack.pop() != tag:
			self.is_valid = False
		

def main():
	file_name = input("Enter file name: ")
	checker = HTMLChecker()
	
	if checker.validate_html_file(file_name):
		print("Valid HTML")
	else:
		print("Invalid HTML, mismatched opening and closing braces")

if __name__ == "__main__":
	main()