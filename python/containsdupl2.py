class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
#         seen = set([])
        
#         for num in nums:
#             if num in seen:
#                 return True
#             seen.add(num)
#         return False
        
        dic = {}
        for i in range(len(nums)):
            if nums[i] in dic.keys() and i != dic[nums[i]] and abs(i-dic[nums[i]]) <= k:
                return True
            dic[nums[i]] = i
        return False
