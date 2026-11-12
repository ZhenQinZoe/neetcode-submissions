class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        best_len = 0
        for i in range(len(nums)):
            len1 = 0
            for j in range(i, len(nums)):
                if nums[j] == 1:
                    len1 += 1
                elif nums[j] == 0:
                    break
            best_len = max(best_len,len1)
        return best_len