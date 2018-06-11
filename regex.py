#regex_sum_42.txt
import re
fname = 'regex_sum_99986.txt' #input("Enter file name: ")
xfile = None
try:
    xfile = open(fname)
except:
    print('Opening file failed')
if xfile != None:
    fileContent = xfile.read()
    numberList = re.findall("[0-9]+",fileContent)
    print(numberList)
    total = 0
    for number in numberList:
        total = total + int(number)

    print('Sum of numbers is:',total)
    #print( sum( [  ('[0-9]+',xfile.read()) ] ) )