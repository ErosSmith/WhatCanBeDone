# -------
# imports
# -------
import warnings
import glob
from itertools import count
from io       import StringIO
from unittest import main, TestCase

from Decorator import fib, cache 
import time

warnings.filterwarnings('ignore')
class TestCollatz (TestCase) :
    # ----
    # read
    # ----

    def test_basic (self) :
    	limit = 10000
    	print("limit is " + str(limit)) 

    	x = count(0)
    	arr = []
    	t1 = time.time() 
    	for num in x:
    		if num == limit:
    			break
    		arr += [fib(num)]
    	t2 = time.time()
    	print (t2 - t1)


    	x = count(0)
    	fib2 = cache(fib)
    	arr2 = []
    	t1 = time.time() 
    	for num in x:
    		if num == limit:
    			break
    		arr2 += [fib2(num)]
    	t2 = time.time()
    	print (t2 - t1)


    	x = count(0)
    	arr3 = []
    	t1 = time.time() 
    	for num in x:
    		if num == limit:
    			break
    		arr3 += [fib2(num)]
    	t2 = time.time()
    	print (t2 - t1)





    	assert(True)


main()