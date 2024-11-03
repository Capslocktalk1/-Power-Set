def totalflips(a,b):
    flips = 0
    while(a > 0 or b > 0):
        t1 = (a & 1)
        t2 = (b & 1)
        if( t1 != t2):
            flips += 1
        a >>= 1
        b >>= 1
        
    return flips

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("total flip needed: ", totalflips(a,b))