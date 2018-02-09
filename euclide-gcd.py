def gcd(a,b):
        if b == 0:
                return b
        else:
                return gcd(b,b%a)
                
def max(a,b):
        if a > b:
                return a
        else:
                return b
                
def min(a,b):
        if a < b:
                return a
        else:
                return b
                
if __name__ == '__main__':
        x, y = input().strip().split(' ')
        x, y = [int(x),int(y)]
        b = max(x,y)
        a = min(x,y)
        print("GCD(%d,%d) = %d"%(b,a,gcd(b,a))
        
