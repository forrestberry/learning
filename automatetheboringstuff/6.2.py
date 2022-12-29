#! python3
# Add bullets to list in clipboard

import sys
import subprocess

def getclipboard():
    return subprocess.check_output('pbpaste', env={'LANG':
                                           'en_US.UTF-8'}).decode('utf-8')

def toclipboard(output):
    process = subprocess.Popen(
    'pbcopy', env={'LANG': 'en_US.UTF-8'}, stdin=subprocess.PIPE)
    process.communicate(output.encode('utf-8'))

text = getclipboard()

text = text.split('\n')
text = ['* ' + x for x in text]

final = '\n'.join(text)

toclipboard(final)
