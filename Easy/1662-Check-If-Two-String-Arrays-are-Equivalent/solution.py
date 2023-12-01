class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        def concat(array):
            if not array:
                return ""
            return array[0] + concat(array[1:])

        str1 = concat(word1)
        str2 = concat(word2)

        return str1 == str2
