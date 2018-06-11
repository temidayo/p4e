# Use words.txt as the file name
fname = input("Enter file name: ")
#fh = open(fname)
xfile = None
#countLine = 0
try:
    xfile = open(fname)
except:
    print('Opening file failed')
if xfile != None:
    for line in xfile:
        #cleanLine = 
        print((line.upper()).rstrip())
        #countLine = countLine + 1
    #print(countLine,'lines')
