# Use the file name mbox-short.txt as the file name
valueAddition = 0.0
lineCount = 0;
fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    else:
        lineCount = lineCount + 1;
        text = line;
        pos = text.find(':')
        #print(pos)
        numericPart = text[pos+1:]
        valueAddition = valueAddition + float(numericPart.strip())
print('Average spam confidence:',valueAddition/lineCount)   