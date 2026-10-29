class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        restored_array = []
        for i in range(0 , len(nums)):
            if nums[i] in restored_array:
                return True
            restored_array.append(nums[i])
        return False

        