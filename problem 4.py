class Solution(object):
    def countHillValley(self, nums):
        filtered = [nums[0]]
        for i in range (1,len(nums)) :
            if nums[i] != nums[i-1] : # filter duplicat numbers 
                filtered.append(nums[i])
       
        count = 0
        for i in range(1, len(filtered) - 1):
            
            
            print ((i))
          
            if filtered[i] > filtered[i-1] and filtered[i] > filtered[i+1]:
               count += 1  # Hill
            elif filtered[i] < filtered[i-1] and filtered[i] < filtered[i+1]:
               count += 1  # Valley

        return count
solution=Solution()       
print(solution.countHillValley([1,2,2,8,7,2,5]))         
