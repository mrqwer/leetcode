# class Solution:
#     def isPerfectSquare(self, n: int) -> bool:
#         if not n or n == 1: return True
#         start = 2
#         stop = n//2
        
#         while start <= stop:
#             tmp = [i for i in range(start, stop+1)]
#             k = tmp[len(tmp)//2]
#             k_squared = k * k
#             if k_squared == n: return True
#             if k_squared > n:
#                 start = tmp[0]
#                 stop = k - 1
#             else:
#                 start = k+1
#                 stop = tmp[-1]
#         return False

class Solution:
  def isPerfectSquare(self, num: int) -> bool:
    l = 1
    r = num

    while l < r:
      m = (l + r) // 2
      if m >= num / m:
        r = m
      else:
        l = m + 1

    return l * l == numclass Solution:
  def isPerfectSquare(self, num: int) -> bool:
    l = 1
    r = num

    while l < r:
      m = (l + r) // 2
      if m >= num / m:
        r = m
      else:
        l = m + 1

    return l * l == num
