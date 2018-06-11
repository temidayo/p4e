def computepay(h,r):
    if h > 40:
        extraHours = h - 40
        return (1.5 * extraHours * r)  + (r * 40)
    else:
        return(r * h)
     

hrs = input("Enter Hours:")
rate = input("Enter Rate:")

p = computepay(float(hrs),float(rate))
print(p)