class Solution:
    def canJump(self, nums: List[int]) -> bool:
        ## T.C = O(n)
        ## S.C = O(1)
        
        if len(nums) == 1:
            return True

        n = len(nums)
        destination = n-1
        curr = n-2

        while curr>=0:
            if curr + nums[curr] >= destination:
                destination = curr
            curr -= 1

        return destination == 0

