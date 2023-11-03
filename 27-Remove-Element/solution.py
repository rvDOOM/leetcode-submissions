class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left = 0
        right = 0

        while right < len(nums):
            if nums[right] != val:
                temp = nums[left]
                nums[left] = nums[right]
                nums[right] = temp
                left += 1
                right += 1
            else:
                right += 1

        return left
