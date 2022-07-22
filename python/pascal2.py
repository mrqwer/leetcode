class Solution:
    def getRow(self, rowIndex: int):
        ans = []

        for i in range(rowIndex+1):
            ans.append([1] * (i+1))

        for i in range(2, rowIndex+1):
            for j in range(1, len(ans[i])-1):
                ans[i][j] = ans[i-1][j-1] + ans[i-1][j]
        return ans[-1]

def main():
    sol = Solution()
    print(sol.getRow(3))

if __name__ == "__main__":
    main()

"""
class Solution:
  def getRow(self, rowIndex: int) -> List[int]:
    ans = [1] * (rowIndex + 1)

    for i in range(2, rowIndex + 1):
      for j in range(1, i):
        ans[i - j] += ans[i - j - 1]

    return ans
"""
