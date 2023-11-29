class Solution:
    def hammingWeight(self, n: int) -> int:
        total = 0
        input = bin(n)
        for i in iter(input[2:]):
            if i == "1":
                total += 1

        return total
