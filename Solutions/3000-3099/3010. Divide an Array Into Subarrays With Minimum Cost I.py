class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        tot = nums[0]
        temp = nums[0]
        nums.sort()
        if nums[0] == temp and nums[0] != nums[1]:
            tot += nums[2]
        else :
            tot += nums[0]
            
        if nums[1] == temp and nums[1] != nums[2] :
            tot += nums[2]
        else :
            tot += nums[1]
        return tot
        
