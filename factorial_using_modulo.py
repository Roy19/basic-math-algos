def factorial(num):
    '''Returns the factorail of the number
    as a modulo of 10^9 + 7'''
    fact = 1
    for i in range(1,num+1):
        fact = (fact*i) % 1000007

    return fact

if __name__ == '__main__':
    num = int(input().strip())
    print("Factorial(%d) = %d"%(num,factorial(num)))

