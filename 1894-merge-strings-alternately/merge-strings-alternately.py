class Solution(object):
    def mergeAlternately(self, word1, word2):

        n=0

        output = ""

        while n <  len(word1) and n < len(word2):
            output = output + word1[n] + word2[n]
            n = n + 1

        if len(word1) > len(word2):
            output = output + word1[n:]

        if len(word2) > len(word1):
            output =  output + word2[n:]

        return output





        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        