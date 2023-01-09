# search the text in your clipboard for phone numbers and email addresses

import copy_paste
import re

text = copy_paste.getclipboard()

# regexes

email = re.compile(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}')

phone = re.compile(r'''(
    (\d{3}|\(\d{3}\))?                # Area code
    (\s|-|\.))?                       # separator
    (\d(3})                           # first 3 digits
    (\s|-|\.))?                       # separator
    (\d{4})                           # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?    # extension
    )''', re.verbose)

# search

emails = email.findall(text)
phoneNums = phone.findall(text)

results = []

results.append(emails)
results.append(phoneNums)

if len(results) == 0:
    copy_paste.toclipboard('No emails or phone numbers in text.')
else:
    finalresult = ', '.join(results)
    copy_paste.toclipboard(finalresult)
