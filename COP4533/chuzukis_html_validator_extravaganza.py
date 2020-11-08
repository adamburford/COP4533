#!/usr/bin/env python3
# It should prompt the user for a file path and then 
# read in the html document found at that location. 
# If the html is valid it should display “Valid HTML”.
# If not, it should say 
#   "Invalid HTML, mismatched opening and closing braces"

import re

VALID_HTML = "Valid HTML"
INVALID_EMPTY = "Is the absence of HTML, valid HTML?"
INVALID_MISMATCH = "Invalid HTML, mismatched opening and closing braces."
INVALID_TAG = "Invalid HTML, not a valid tag."
VOID_TAGS = frozenset( (\
    'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', \
    'link', 'meta', 'param', 'source', 'track', 'wbr' \
) )

def main():

    # prompt user for filepath
    html_filepath = 'index.html' # input()

    # read html into string
    html_string = ''
    with open(html_filepath, 'r') as f:
        html_string = f.read()

    # parse html for a list of all tags, open and close
    tag_list = getAllTags(html_string)

    # if valid, output “Valid HTML”
    try:
        validate_html(tag_list)
        print(VALID_HTML)
    except Exception as e:
        print(e)


def getAllTags(html_string):
    p = re.compile('<.*?>')
    return p.findall(html_string)


def validate_html(tag_list):

    if len(tag_list) == 0:
        raise Exception(INVALID_EMPTY)

    tag_stack = []
    for tag in tag_list:

        # if void tag, skip since it doesn't have a closing tag anyways
        if is_void_tag(tag):
            continue

        # if closing tag, check if a matching open tag was the most recent
        if is_closing_tag(tag):

            # get corresponding opening tag
            opening_tag = get_opening_tag(tag)

            if len(tag_stack) > 0 and tag_stack[-1] == opening_tag:
                tag_stack.pop()
            else:
                raise Exception(INVALID_MISMATCH)
        else:
            # strip out attributes and stuff so it's just the tag name
            # e.g. '<span class="asdf">' to '<span>'
            # don't bother with this on closing tags, because
            #   '</span class="asdf">' isn't a thing and should fail
            tag = strip_tag(tag)
            
            # push opening tag onto stack
            tag_stack.append(tag)


def get_opening_tag(tag):

    if is_closing_tag(tag):
        return tag[:1] + tag[2:]

    return tag


def is_closing_tag(tag):

    return len(tag) > 3 and tag[1] == '/'


def strip_tag(tag):

    index_of_first_space = tag.find(' ')
    return tag[:index_of_first_space] + '>'


def is_void_tag(tag):

    # if the tag is long enough and not a closing tag
    # e.g. '<br />', not '<>' or '</br>'
    if len(tag) > 3 and tag[1] != '/':

        # remove that optional trailing slash
        # e.g. '<br />' to `br `
        index_of_last_slash = tag.rfind('/')
        tag = tag[1:index_of_last_slash]

        # strip spaces from the end.
        # e.g. 'br ' to 'br'
        tag = tag.rstrip()

        return tag in VOID_TAGS
    else:
        return False


if __name__ == "__main__":
    main()