def exponent(num,pow):
	if pow == 0:
		return 1
	elif pow == 1:
		return num
	elif pow % 2 == 0:
		return exponent(num,pow//2)**2
	else:
		return num*(exponent(num,(pow-1)//2)**2)

def modularExponent(num,pow,M=(10**9)+7):
    if pow == 0:
        return 1
    elif pow == 1:
        return num % M
    elif pow % 2 == 0:
        return (modularExponent(num,pow//2,M)**2) % M
    else:
        return (num*(modularExponent(num,pow//2,M)**2)) % M
		
if __name__ == '__main__':
	n,p = input().strip().split(' ')
	n,p = [int(n),int(p)]
	print("n^p = %d"%(modularExponent(n,p)))
	
