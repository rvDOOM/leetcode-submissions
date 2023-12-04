class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        left = res = 0
        right = k - 1
        currSum = sum(arr[left:right])

        while right < len(arr):
            currSum += arr[right]
            if currSum // k >= threshold:
                res += 1
            currSum -= arr[left]
            left += 1
            right += 1

        return res
