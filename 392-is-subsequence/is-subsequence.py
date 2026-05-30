class Solution(object):
    def isSubsequence(self, s, t):
        pos = 0

        if len(s) == 0:
            return True

        for i in range(len(t)):

            if t[i] == s[pos]:
                pos = pos + 1

                if pos == len(s):
                    return True

        return False