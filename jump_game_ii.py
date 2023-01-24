class Solution:
    def jump(self, nums: List[int]) -> int:
        ## approach 2: greedy
        ## T.C = O(n)
        ## S.C = O(1)
        n = len(nums)
        if n <= 1:
            return 0

        curr_interval = nums[0]
        next_interval = nums[0]
        jumps = 1

        for i in range(1, len(nums)):
            next_interval = max(next_interval, i + nums[i])
            if i < n - 1 and i == curr_interval:
                curr_interval = next_interval
                jumps += 1
        
        return jumps

        ## approach 1: bfs
        ## T.C = exponential
        n = len(nums)
        if n <= 1:
            return 0
        q = [0]
        hs = set()
        jumps = 0

        while q:
            for i in range(len(q)):
                idx = q.pop(0)
                for j in range(1, nums[idx]+1):
                    new_idx = idx + j
                    if new_idx == n - 1:
                        return jumps + 1
                    if new_idx not in hs:
                        q.append(new_idx)
                        hs.add(new_idx)
            
            jumps += 1
        
        return -1


