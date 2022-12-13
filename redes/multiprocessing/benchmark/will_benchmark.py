"""
Testing python multiprocessing speed. Based on
http://blogs.warwick.ac.uk/dwatkins/entry/benchmarking_parallel_python_1_2/
https://gist.github.com/willtownes/2762ba1dd73fb03ecdb24d625aa27b58
"""

import time
import math
import multiprocessing as mp

def isprime(n):
    """Returns True if n is prime and False otherwise"""
    if not isinstance(n, int):
        raise TypeError("argument passed to is_prime is not of 'int' type")
    if n < 2:
        return False
    if n == 2:
        return True
    max = int(math.ceil(math.sqrt(n)))
    i = 2
    while i <= max:
        if n % i == 0:
            return False
        i += 1
    return True

def sum_primes(n):
    """Calculates sum of all primes below given integer n"""
    return sum([x for x in xrange(2,n) if isprime(x)])

if __name__=="__main__":
    inputs = range(100000, 1000000, 100000)
    n_cpu = mp.cpu_count()
    pool = mp.Pool(n_cpu)

    print("\nParallel processing with %d cores"%n_cpu)
    start_time = time.time()
    jobs = zip(inputs, pool.map(sum_primes,inputs))
    for input, job in jobs:
        print ("Sum of primes below", input, "is", job)
    print (f'Time elapsed: {time.time() - start_time} s')

    print("\nSerial processing")
    start_time = time.time()
    for x in inputs:
        print ("%d: %d" % (x, sum_primes(x)))
    print (f'Time elapsed: {time.time() - start_time} s')
