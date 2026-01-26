class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        min_abs = inf
        for i in range(len(arr)-1) :
            if abs(arr[i] - arr[i+1]) < min_abs :
                min_abs = abs(arr[i] - arr[i+1])
        ans = [] 
        for i in range(len(arr)-1) :
            if abs(arr[i] - arr[i+1]) == min_abs :
                ans.append(list(arr[i: i+2]))
        return ans
            
        
