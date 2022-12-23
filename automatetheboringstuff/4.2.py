# Write a function that takes a list value as an argument and returns a string
# with all the items separated by a comma and a space, with and inserted before
# the last item.

#spam = ['apples', 'bananas', 'tofu', 'cats']
#spam = ['apples', 'bananas']
#spam = ['apples']
spam = []

strSpam = ''

if len(spam) > 1:
    for i in spam[:-1]:
        strSpam += i + ' '
    strSpam += 'and ' + spam[-1]
elif len(spam) == 1:
    strSpam = spam[0]

print(strSpam)
        

