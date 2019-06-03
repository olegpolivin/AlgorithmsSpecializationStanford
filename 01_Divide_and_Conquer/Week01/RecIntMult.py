print('Welcome to exercise 1: Stanford Algorithms')
print('Input: two n-digit positive integers x and y')
print('Assumption: n is a power of 2')

x = input('Enter first integer: ')
y = input('Enter second integer: ')

n = len(x)
assert len(x) == len(y), 'Digits are not of the same length'
assert n % 2 == 0, 'n is not power of 2'

def RecIntMultiplication(x,y,n):

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
        
        ac = RecIntMultiplication(a,c,n//2)
        ad = RecIntMultiplication(a,d,n//2)
        bc = RecIntMultiplication(b,c,n//2)
        bd = RecIntMultiplication(b,d,n//2)

        return 10**n * ac + 10**(n/2)*(ad+bc) + bd


print('Result of recursive multiplication: ', RecIntMultiplication(x,y,n))