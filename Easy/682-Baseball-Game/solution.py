class Solution:
    def calPoints(self, operations: List[str]) -> int:
        solStack = []

        for x in operations:
            print(x)

            if x == "+":
                solStack.append(solStack[-2] + solStack[-1])
            elif x == "D":
                solStack.append(solStack[-1] * 2)
            elif x == "C":
                solStack.pop()
            else:
                solStack.append(int(x))

        total = 0
        for x in range(len(solStack)):
            total += solStack[-1]
            solStack.pop()

        return total
