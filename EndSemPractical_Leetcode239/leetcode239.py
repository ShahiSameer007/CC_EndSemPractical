class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0
        r = l+k
        ans = []
        while r <= len(nums):
            ans.append(max(nums[l:r]))
            l+=1
            r+=1
        return ans