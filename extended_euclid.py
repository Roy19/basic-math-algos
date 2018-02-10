d = 0
x = 0
y = 0

def extendedEuclid(A,B):
    global d,x,y
    
    if B == 0:
        d = A
        x = 1
        y = 0
    else:
        extendedEuclid(B,A%B)
        temp = x
        x = y
        y = temp - (A//B)*y

if __name__ == '__main__':
    extendedEuclid(5,3)
    print("GCD(5,3) = %d"%(d))
    extendedEuclid(50,40)
    print("GCD(50,40) = %d"%(d))