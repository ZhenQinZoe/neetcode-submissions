class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        hashmap = {0:1}
        pre = 0
        count = 0
        for i in range(len(nums)):
            pre += nums[i]
            diff = pre- goal
            count += hashmap.get(diff,0)
            hashmap[pre] = hashmap.get(pre,0)+1
        return count
        