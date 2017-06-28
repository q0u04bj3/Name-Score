"""
file = ["CDEF","ABC","FIJK"]
file = sorted(file)
"""

import re
pat = '[A-Z]+'

name_file = open("name.dat","r")
names_file = name_file.read()
file = sorted(re.findall(pat, names_file))


for index, element in enumerate(file):
    sum=0
    for letter in element:
        sum+=(ord(letter)-64)

        print sum*(index+1)
