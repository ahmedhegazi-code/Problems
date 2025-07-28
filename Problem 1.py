class Solution(object):
    def twoSum(self, nums, target):
        seen = {}  
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
        for i, num in enumerate(nums):  
            complement = target - num 
            if complement in seen :
                return [seen[complement],i]
            seen[num]=i

            


solution = Solution()
print(solution.twoSum(([1,2,3,4]),5))  


               