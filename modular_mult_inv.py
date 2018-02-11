def modular_multplicative_inverse(A,M):
    A = A%M

    for B in range(1,M):
        if (A*B)%M == 1:
            return B

if __name__ == '__main__':
    x = modular_multplicative_inverse(5,12)
    y = modular_multplicative_inverse(17,19)
    print("Modular multiplicative inverse of A = 5 and M = 12 is: %d" %(x))
    print("Modular multiplicative inverse of A = 17 and M = 19 is: %d" %(y))