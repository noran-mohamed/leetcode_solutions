class Solution:
    def maxSumTrionic(self, nums: List[int]) -> int:
        INF = -(1 << 50)
        res = a = b = c = INF
        prev = nums[0]

        for i in range(1, len(nums)) :
            cur = nums[i]
            na = nb = nc = INF

            if cur > prev :
                na = max(a, prev) + cur 
                nc = max(b, c) + cur

            elif cur < prev :
                nb = max(a, b) + cur
            
            a, b, c = na, nb, nc
            res = max(res, c)
            prev = cur
        return res


        
