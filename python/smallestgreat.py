class Solution:
	def nextGreatestLetter(self, letters, target: str) -> str:
		if target >= max(letters):
			return min(letters)
		i = 0
		while min(letters) <= target:
			letters.pop(letters.index(min(letters)))
		return min(letters)

def main():
	sol = Solution()
	return sol.nextGreatestLetter(['c', 'f', 'j'], 'd')
if __name__ == "__main__":
	print(main())
		
