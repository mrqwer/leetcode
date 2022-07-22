class Solution:
	def search(self, nums, target: int) -> int:
		l = 0
		r = len(nums)-1
		while l <= r:
			mid = (l+r)//2
			if target == nums[mid]:
				return mid
			elif target < nums[mid]:
				r = mid - 1
			else:
				l = mid + 1
		return -1
		

def main():
	sol = Solution()
	return sol.search([2, 5], 5)

if __name__ == "__main__":
	print(main())
				
