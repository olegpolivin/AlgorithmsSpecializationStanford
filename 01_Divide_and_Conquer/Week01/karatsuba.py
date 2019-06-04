from math import ceil

print('Welcome to exercise 2: Stanford Algorithms')
print('Input: two n-digit positive integers x and y')
print('Output: the product x*y calculated recursively')
print('Assumption: n is a power of 2')

x = input('Enter first integer: ')
y = input('Enter second integer: ')

n = max(len(x), len(y))

n1, n2 = len(x), len(y)
assert n1 % 2 == 0, 'Number of digits in the first number is not power of 2'
assert n2 % 2 == 0, 'Number of digits in the second number is not power of 2'


def KaratsubaMultiplication(x,y,n):

    """
    Function to multiply two n-digits recursively
    """

    if n == 1 :
        x = int(x)
        y = int(y)
        return x * y 
    
    else : 

        k = ceil(n/2)
        a = x[0:-k]
        b = x[-k:]

        if len(a) == 0:
            a = '0'
        
        c = y[0 : -k]
        d = y[-k:]

        if len(c)==0:
            c = '0'
        
        p = str(int(a) + int(b))
        q = str(int(c) + int(d))

        ac = KaratsubaMultiplication(a,c,k)
        bd = KaratsubaMultiplication(b,d,k)
        pq = KaratsubaMultiplication(p,q,k)
        
        
        adbc = pq - ac - bd      
    
        return 10**(n)* ac + 10**(k)* adbc + bd

res = KaratsubaMultiplication(x,y,n)
print('Result of Karatsuba multiplication: ', res)
print('Calculation is correct: ', res == int(x)*int(y))