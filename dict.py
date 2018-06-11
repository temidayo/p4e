name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
#count = 0
emails = dict()
for line in handle:
    if line.startswith('From '):
        words = line.split()
        #print(words[1])
        emails[words[1]] = emails.get(words[1],0) + 1
        #count = count + 1;

maxEmailKey = None
maxEmailValue = None
for emailKey, emailValue in emails.items():
    if maxEmailValue is None or emailValue > maxEmailValue:
        maxEmailValue = emailValue
        maxEmailKey = emailKey
print(maxEmailKey,maxEmailValue)
