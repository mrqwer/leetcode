class Solution:
	def isPalindrome(x: int) -> bool:
		if x < 0: return False
		n = 0
		k = x
		while k:
			n = n*10 + k%10
			k //= 10
		return n == x
