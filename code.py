"""
This is the code file for Assignment from 23rd August 2017.
This is due on 30th August 2017.
"""
##################################################
#Complete the functions as specified by docstrings


# 1
def entries_less_than_ten(L):
    """
    Return those elements of L which are less than ten.

    Args:
        L: a list

    Returns:
        A sublist of L consisting of those entries which are less than 10.
    """
    return [i for i in L if i<10]

#Test
#print entries_less_than_ten([2, 13, 4, 66, -5]) == [2, 4, 6, -5]



# 2
def number_of_negatives(L):
    """
    Return the number of negative numbers in L.

    Args:
        L: list of integers

    Returns:
        number of entries of L which are negative
    """
    return len([i for i in L if i<0])

# TEST
#print number_of_negatives([2, -1, 3, 0, -1, 0, -45, 21]) == 3



# 3
def common_elements(L1, L2):
    """
    Return the common elements of lists ``L1`` and ``L2``.

    Args:
        L1: List
        L2: List

    Returns:
        A list whose elements are the common elements of ``L1`` and
        ``L2`` WITHOUT DUPLICATES.
    """
    L_common = [j for i in L1 for j in L2 if i==j]
    L_unique = []
    for i in L_common:
        if i not in L_unique:
            L_unique.append(i)
    return L_unique

#TEST
#common_elements([1, 2, 1, 4, "bio", 6, 1], [4, 4, 2, 1, 3, 5]) == [1, 2, 4]



#4
def fibonacci_generator():
    """
    Generate the Fibonacci sequence.

    The Fibonacci sequence 1, 1, 2, 3, 5, 8, 13, 21,...
    is defined by a1=1, a2=1, and an = a(n-1) + a(n-2).
    """
    a1=1
    a2=1
    while True:
        yield a1
        atemp=a1 
        a1=a2
        a2= atemp+a2     
        
#TEST
#f = fibonacci()
#[f.next() for i in range(10)] == [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]



#5
def largest_fibonacci_before(n):
    """
    Return the largest Fibonacci number less than ``n``.
    """
    L=[]
    f=fibonacci_generator()
    a=f.next()
    while a < n:
        largest_fib=a 
        a=f.next()
    return largest_fib

#TEST
#largest-fibonacci_before(55) == 34



#6
from math import factorial
def catalan_generator():
    """
    Generate the sequence of Catalan numbers.

    For the definition of the Catalan number sequence see `OEIS <https://www.oeis.org/A000108>`.
    """
    n=0
    while True:
        yield factorial(2*n)/(factorial(n)*factorial(n+1))
        n+=1

#TEST
#c = catalan_generator()
#[c.next() for i in range(10)] == [1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862]

    
    
#7
from math import sqrt 
from fractions import gcd
def primitive_pythagorean_triples_less_than_n(n):
    """
    Return the primitive pythagorean triples less than an integer ''n''. 
    A Pythagorean triple consists of three positive integers a, b, and c, such that a**2 + b**2 = c**2.
    A primitive Pythagorean triple is one in which a, b and c are prime to each other.

    Args:
        n: integer

    Returns:
        List of the pythagorean triples less than ''n''.
    """
    L=[]
    for x in range(1,n):
        for y in range(x,n):
            z=sqrt(x**2 + y**2)
            if gcd(int(x),int(y))==1:
                if int(z)**2==z**2 and z<n:
                    L.append({x, y, int(z)})
    return L

#TEST          
#primitive_pythagorean_triplets_less_than_n(20) == [{3, 4, 5}, {5, 12, 13}, {8, 15, 17}]

