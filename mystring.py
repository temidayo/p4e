text = "X-DSPAM-Confidence:    0.8475";
pos = text.find(':')
#print(pos)
numericPart = text[pos+1:]
print(float(numericPart.strip()))