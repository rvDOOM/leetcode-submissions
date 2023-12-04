class Solution:
    def largestGoodInteger(self, num: str) -> str:
        currMax = ""
        left = right = 0

        while right <= len(num) - 1:
            if num[left] != num[right]:
                left = right
            right += 1
            if right - left == 3:
                if currMax < num[left:right]:
                    currMax = num[left:right]

        return currMax
