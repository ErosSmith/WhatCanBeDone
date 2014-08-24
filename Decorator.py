# def cache(fuct):	
# 	dic = {}
	
# 	def f(*args):	
# 		arg = args[0]
# 		if arg in dic :
# 			return dic[arg]
# 		temp = fuct(arg,dic)
# 		dic[arg] = temp
# 		return temp
# 	return f

def fib(*args):

	assert(len(args)>0 and len(args)< 3)
	assert(type(args[0]) is type(0))

	
	if(len(args) == 2):
		assert(type(args[1]) == type({}))
		fib_dic = args[1]
	else:
		fib_dic = {}

	limit = args[0]

	# print(fib_dic)

	if fib_dic != {} and fib_dic['last_entry'] > 1:
		big_key = fib_dic['last_entry']
		second_key = big_key - 1
		# print("last entry is " + str(fib_dic['last_entry'])+ ' num is ' + str(limit))
		result = fib_dic[big_key]
		prev = fib_dic[second_key]
		i = big_key + 1
		
	else:
		prev = -1
		result = 1
		total = 0
		i = 0
		fib_dic['last_entry'] = 0



	

	# print("prev is " + str(prev))
	# print("result is " + str(result))
	# print("i is " + str(i))
	# print('limit is ' + str(limit))


	while limit >= i:
		total = result + prev
		prev = result
		result = total
		fib_dic[i] = total
		# print('added ' +str(i)+' : ' +str(total)+' to dic')
		i += 1
	fib_dic['last_entry'] = limit
	return result

class cache :
    def __init__ (self, f) :
        self.f = f
        self.d = {}
        self.d['last_entry'] = 0


    def __call__ (self, *args) :
        
        k = args[0]

        if k in self.d :
            return self.d[k]
        v = self.f(k,self.d)
        self.d[k] = v
        self.d['last_entry'] = k
        return v