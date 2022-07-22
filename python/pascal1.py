class Solution:
	def generate(self, numRows: int):
		ans = []

		for i in range(numRows):
		  ans.append([1] * (i + 1))

		for i in range(2, numRows):
		    for j in range(1, len(ans[i]) - 1):
                print("(i - 1)(j - 1) : " + str(ans[i-1][j-1]))
                print("(i-1)(j): " + str(ans[i-1][j]))
			    ans[i][j] = ans[i - 1][j - 1] + ans[i - 1][j]

		return ans

def main():
	sol = Solution()
	print(sol.generate(5))


if __name__ == "__main__":
    main()
