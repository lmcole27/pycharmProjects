# Python code to remove whitespace
import string

def remove(string):
    return string.translate(None, ' \n\t\r')


word = ' g e e k '
new = word.translate(' \n\t\r')
print(word)
print(new)

# Driver Program
# 
# print(remove(word))

# string = 'South Australia'
# print(remove(string))