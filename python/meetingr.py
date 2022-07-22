class Solution:
	def can_attend_meetings(self, intervals) -> bool:
		intervals = sorted(intervals, key=lambda x: x[0])
		
		for i in range(len(intervals)-1):
			if intervals[i][1] > intervals[i+1][0]:
				return False
		return True

def main():
	sol = Solution()
	print(sol.can_attend_meetings([(5, 8), (9, 15)]))

if __name__ == "__main__":
	main()
