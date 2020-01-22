
from typing import Optional, Sequence


def kmp_algo(inp_string: str, substr: str):
	"""
	Implementation of Knuth-Morrison-Pratt algorithm

	:param inp_string: String where substr is to be found (haystack)
	:param substr: substr to be found in inp_string (needle)
	:return: index where first occurrence of substr in inp_string started or None if not found
	"""


	print(inp_string, substr)
	prefixes = prefix_fun(substr)
	print(prefixes)
	i = 0
	j = 0
	while i in range(len(inp_string)) and j in range(len(substr)):
		if inp_string[i] == substr[j]:
			i+=1
			j+=1
		elif j <= 0:
			i+=1
		else:
			j = prefixes[j-1]
		# print(len(inp_string), i, len(substr)-1, j)
		if j >= (len(substr)-1):
			return i - j	
	return None

def prefix_fun(prefix_str: str) -> Sequence[int]:
	"""
	Prefix function for KMP

	:param prefix_str: dubstring for prefix function
	:return: prefix values table
	"""
	l = 0
	lps = [0]*len(prefix_str)
	i = 1

	# the loop calculates lps[i] for i = 1 to M-1 
	while i < len(prefix_str): 
		if prefix_str[i]== prefix_str[l]: 
			l += 1
			lps[i] = l
			i += 1
		else: 
		# This is tricky. Consider the example. 
		# AAACAAAA and i = 7. The idea is similar  
		# to search step. 
			if l != 0: 
				l = lps[l-1] 
				# Also, note that we do not increment i here 
			else: 
				lps[i] = 0
				i += 1
	return lps

if __name__ =='__main__':
	
	# haystack = "ATATCATATC"
	# needle = "ATATC" #6
	# print(kmp_algo(haystack, needle)) # 0 
	# haystack = "ATTATGATGATC"
	# needle = "ATGATC" #6
	# print(kmp_algo(haystack, needle)) # 0 
	# haystack = "Hello, tiny world!"
	# needle = "Hell"
	# print(kmp_algo(haystack, needle)) # 0 
	haystack = "All these moments will be lost in time..."
	needle = "time..."
	print(kmp_algo(haystack, needle)) # 34
	# haystack = "Шел я лесом, вижу мост, на мосту ворона сохнет. " \
	# 			"Взял ее за хвост, положил под мост, пускай ворона мокнет."
	# needle = "Взял"
	# print(kmp_algo(haystack, needle)) #
	# haystack = "Because only a ginger can call another ginger ginger!"
	# needle = "afroamerican"
	# print(kmp_algo(haystack, needle)) # None
