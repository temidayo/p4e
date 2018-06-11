x = 2
if x < 2:
    print('smaller')
elif x < 10:
    print('Medium')

try:
    print(10/2);print(10/5)
except:
    print('Division by zero not allowed')
print ('All done')


...
hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Rate:")
r = float(rate)
if h > 40:
    extraHours = h - 40;
    print((1.5 * extraHours * r)  + (r * 40))
else:
    print(r * h)
...

score = input("Enter Score: ")
fscore = float(score)

if fscore < 0.0:
    print('Too low')
elif fscore > 1.0:
    print('Too High')
else:
    if fscore >= 0.9:
        print('A');
    elif fscore >= 0.8:
        print('B')
    elif fscore >= 0.7:
        print('C')
    elif fscore >= 0.6:
        print('D')
    elif fscore < 0.6:
        print('F')
    