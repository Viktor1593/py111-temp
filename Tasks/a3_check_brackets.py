def check_brackets(brackets_row: str) -> bool:
	"""
	Check whether input string is a valid bracket sequence
	Valid examples: "", "()", "()()(()())", invalid: "(", ")", ")("
	:param brackets_row: input string to be checked
	:return: True if valid, False otherwise
	"""
	a_b = 0
	b_b = 0
	for chr in brackets_row:
		if chr == '(':
			a_b += 1
		elif chr == ')':
			b_b += 1
		if b_b > a_b:
			return False
	return a_b == b_b
