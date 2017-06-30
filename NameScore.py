import re

pat = '[A-Z]+'
score =[]

def NameScore(file):
    with open(file) as file:
        lines = file.readline()

    sortedFile = sorted(re.findall(pat, lines))

    for index, element in enumerate(sortedFile):
        score.append(sum([ord(letter)-64 for letter in element])*(index+1))

    return score
