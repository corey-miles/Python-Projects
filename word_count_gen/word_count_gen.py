'''
    Script using a text file, reads each word into a
        dictionary, then output an HTML file in a Tag Cloud
        format.

    ** Project based on a course project **
    CSS file created by dept.
'''

import os
from utils import FileParser
from web import MarkupParser

#################
## MAIN SCRIPT ##
#################

# Get .txt path

text = input('Enter file to read: ')

while not os.path.exists(text):
    print('ERROR: File does not exist...')
    text = input('Enter file to read: ')

# Utilize FileParser

f_parser = FileParser(text)
f_parser.parse_file()

main_dict = f_parser.words_dict

# Sort words by value

main_dict = sorted(main_dict.items(), key=lambda x: x[1], reverse=True)

# Get length

LENGTH = -1

while LENGTH < 0:
    try:
        LENGTH = int(input('Enter number of words: '))
        if LENGTH < 0:
            print('ERROR: Value cannot be negative...')
    except ValueError:
        print('ERROR: Cannot convert to int...')

# Grab requested words and sort by key

sub_dict = main_dict[:LENGTH]
maximum = sub_dict[0][1]
minimum = sub_dict[LENGTH-1][1]

sub_dict = sorted(sub_dict)

# Get .html path

html = input('Enter file [.html] to create: ')

while not html.endswith('.html'):
    print('ERROR: Missing .html extension...')
    html = input('Enter file [.html] to create: ')

# Utilize MarkupParser

m_parser = MarkupParser(html, text, sub_dict, maximum, minimum, LENGTH)
m_parser.create_html()

# Inform of new file

print("New File: " + html)
