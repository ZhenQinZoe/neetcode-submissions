class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        best_len = 0
        cnt = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                cnt +=1
            else:
                cnt = 0
            best_len = max(best_len,cnt)
        return best_len