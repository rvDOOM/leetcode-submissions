class Solution:
    def isValid(self, s: str) -> bool:
        sol = []

        for i in range(len(s)):
            if s[i] == ")" and sol[-1] == "(":
                sol.pop()
            elif s[i] == "}" and sol[-1] == "{":
                sol.pop()
            elif s[i] == "]" and sol[-1] == "[":
                sol.pop()
            else:
                sol.append(s[i])

        return not sol
