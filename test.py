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
from random import randint

warnings.filterwarnings('ignore')
class TestCollatz (TestCase) :
    # ----
    # read
    # ----

    def test_basic (self) :
    	limit = 100
    	print("limit is " + str(limit)) 

    	x = range(limit)
    	
    	arr = []
    	t1 = time.time() 
    	for num in x:
    		# print("num is "+str(num))
    		arr += [fib(num)]
    	t2 = time.time()
    	print (t2 - t1)


    	fib2 = cache(fib)
    	arr2 = []
    	t1 = time.time() 
    	for num in x:
    		# print("num is "+str(num))
    		arr2 += [fib2(num)]
    	t2 = time.time()
    	print (t2 - t1)
 
    	arr3 = []
    	t1 = time.time() 
    	for num in x:
    		# print("num is "+str(num))
    		arr3 += [fib2(num)]
    	t2 = time.time()
    	print (t2 - t1)

    	# print(arr)
    	# print(arr2)


    	assert(arr == arr2)
    	assert(arr == arr3)
    	assert(arr3 == arr2)
    
    def test_random (self) :

    	rand_arr = []
    	
    	for i in range(50):
    		rand_arr += [randint(0, 10000)]

    	

    	# rand_arr = [2, 5, 11, 8]
    	# print(rand_arr)

    	fib2 = cache(fib)

    	ans_arr1 = []
    	ans_arr2 = []
    	ans_arr3 = []

    	t1 = time.time() 

    	for num in rand_arr:
    		ans_arr1 += [fib(num)]

    	t2 = time.time()
    	print (t2 - t1)

    	t1 = time.time() 

    	for num in rand_arr:
    		ans_arr1 += [fib2(num)]

    	t2 = time.time()
    	print (t2 - t1)

    	t1 = time.time() 

    	for num in rand_arr:
    		ans_arr1 += [fib2(num)]

    	t2 = time.time()
    	print (t2 - t1)
   

main()