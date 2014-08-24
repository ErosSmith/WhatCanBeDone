def cache(fuct):
	dic = {}
	def f(arg):
		if arg in dic :
			return dic[arg]
		temp = fuct(arg)
		dic[arg] = temp
		return temp
	return f

def fib(num):

	prev = -1
	result = 1
	total = 0
	i = 0
	while num >= i:
		total = result + prev
		prev = result
		result = total
		i += 1
	return result
