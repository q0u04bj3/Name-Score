file = ["CDEF","ABC","FIJK"]
file = sorted(file)

for index, element in enumerate(file):
    sum=0
    for letter in element:
        sum+=(ord(letter)-64)

    print sum*(index+1)

#    print int(ord(file[index][element]))-64