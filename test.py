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

    	x = count(0)
    	arr = []
    	t1 = time.time() 
    	for num in x:
    		if num == 40:
    			break
    		arr += [fib(num)]
    	print(arr)
    	t2 = time.time()
    	print (t2 - t1)


    	x = count(0)
    	fib2 = cache(fib)
    	arr2 = []
    	t1 = time.time() 
    	for num in x:
    		if num == 40:
    			break
    		arr2 += [fib2(num)]
    	print(arr2)
    	t2 = time.time()
    	print (t2 - t1)


    	x = count(0)
    	arr3 = []
    	t1 = time.time() 
    	for num in x:
    		if num == 40:
    			break
    		arr3 += [fib2(num)]
    	print(arr3)
    	t2 = time.time()
    	print (t2 - t1)





    	assert(True)

print("wtf")

main()