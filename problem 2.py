class Selution(object):
    def twoSum(self,nums,target):
        seen = {}
        for i,num in enumerate (nums) :
            newnum = target - num 
            if newnum in seen :
                return [seen[newnum],i]
            seen[num] = i 

solution = Selution()
print(solution.twoSum(([1,2,3,4]),6))

