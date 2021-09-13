"""
This task is optional.
Write a generator that takes a number N as an input
and returns a generator that yields N FizzBuzz numbers*
Don't use any ifs, you can find an approach for the implementation
in this video**.
Definition of done:
 - function is created
 - function is properly formatted
 - function has tests
* https://en.wikipedia.org/wiki/Fizz_buzz
** https://www.youtube.com/watch?v=NSzsYWckGd4
"""


def divisible(n: int, div: int):
    return n % div == 0


def fizzbuzz(n: int):
    '''
    >>> list(fizzbuzz(5))
    ['1', '2', 'fizz', '4', 'buzz']
    '''
    ans = [str, lambda x: 'fizz', lambda x: 'buzz',
           lambda x: 'fizzbuzz']
    for number in range(1, n+1):
        idx = int(divisible(number, 3)) + int(2*divisible(number, 5))
        yield ans[idx](number)
