name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
times = dict()
for line in handle:
    if line.startswith('From '):
        words = line.split()
        timePiece = words[5].split(':')
        #print(words[1])
        times[timePiece[0]] = times.get(timePiece[0],0) + 1
        #count = count + 1;
        
sortedList = sorted([(k,v) for k,v in times.items()])
#print(sortedList)

for k,v in sortedList:
    print(k,v)