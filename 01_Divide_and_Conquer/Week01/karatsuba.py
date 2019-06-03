print('Welcome to exercise 2: Stanford Algorithms')
print('Input: two n-digit positive integers x and y')
print('Output: the product x*y calculated recursively')
print('Assumption: n is a power of 2')

x = input('Enter first integer: ')
y = input('Enter second integer: ')

n = len(x)
assert len(x) == len(y), 'Digits are not of the same length'
assert n % 2 == 0, 'n is not power of 2'


def KaratsubaMultiplication(x,y,n):

    """
    Function to multiply two n-digits recursively
    """

    if n == 1 :
        x = int(x)
        y = int(y)
        return x * y 
    
    else : 

        a = x[0:n//2]
        b = x[n//2:]
        c = y[0:n//2]
        d = y[n//2 :]
        
        p = str(int(a) + int(b))
        q = str(int(c) + int(d))

        ac = KaratsubaMultiplication(a,c,n//2)
        bd = KaratsubaMultiplication(b,d,n//2)
        pq = KaratsubaMultiplication(p,q,n//2)

        adbc = pq - ac - bd      

        return 10**n * ac + 10**(n/2)*(adbc) + bd


print('Result of Karatsuba multiplication: ', KaratsubaMultiplication(x,y,n))