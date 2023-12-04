class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        totalSecs = 0
        prevX = points[0][0]
        prevY = points[0][1]
        inputs = points[1:]

        for i in range(len(inputs)):
            newX = inputs[i][0]
            newY = inputs[i][1]

            totalMoveX = abs(prevX - newX)
            totalMoveY = abs(prevY - newY)

            totalSecs += max([totalMoveX, totalMoveY])
            prevX = newX
            prevY = newY

        return totalSecs
