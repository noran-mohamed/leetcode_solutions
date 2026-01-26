class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        sorted_nums = sorted(nums)
        ans = 10000000
        n = len(nums)
        for i in range(n) :
            if i+k-1 >= n :
                break
            temp = sorted_nums[i+k-1] - sorted_nums[i]
            if temp < ans :
                ans = temp
        return ans
        
