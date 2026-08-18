class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        mx = 0
        cnt = 0
        l,n = 0,len(nums)
        while l < n:
            if nums[l] == 1:
                cnt += 1
                l+=1
            else:
                mx = max(cnt,mx)
                l+=1
                cnt = 0
        mx = max(cnt,mx)
        return mx
