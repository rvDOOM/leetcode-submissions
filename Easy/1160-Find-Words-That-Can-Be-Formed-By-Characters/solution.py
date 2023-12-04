class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        charsDict = defaultdict()
        sol = 0

        for i in range(len(chars)):
            if chars[i] in charsDict:
                charsDict[chars[i]] += 1
            else:
                charsDict[chars[i]] = 1

        for i in range(len(words)):
            tempDict = dict(charsDict)
            for j in range(len(words[i])):
                if words[i][j] in tempDict:
                    sol += 1
                    tempDict[words[i][j]] -= 1
                    if tempDict[words[i][j]] == 0:
                        del tempDict[words[i][j]]
                    continue
                else:
                    sol -= j
                    break

        return sol
