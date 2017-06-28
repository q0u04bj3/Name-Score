import re
pat = '[A-Z]+'

name_file = open("name.dat","r")
names_file = name_file.read()
file = sorted(re.findall(pat, names_file))


for index, element in enumerate(file):
    print sum([ord(letter)-64 for letter in element])*(index+1)
