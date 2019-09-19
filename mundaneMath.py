import numpy as np
def mundaneMath(first_num, last_num):
	sum=0
	for i in range(first_num, last_num+1):
		'''
		The latter number is last_num+1 bc range function doesn't count the last number.
		'''
		if i%2 == 0:
			sum = sum + i
		else:
			continue
	print(sum)
	return sum

if __name__ == "__main__":
	mundaneMath(1, 100)
	
