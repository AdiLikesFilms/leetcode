class Solution(object):
    def reverseVowels(self, s):

        n = len(s)
        pos = 0
        pos2 = 0
        extra = ""

        for i in range(n):
            if s[i] in 'aeiouAEIOU':
                extra = extra + s[i]

        extra = extra[::-1]

        s = list(s)

        for e in range(n):

            if s[e] not in 'aeiouAEIOU':
                s[pos] = s[e]
                

            else:
                s[pos] = extra[pos2]
                pos2 += 1

            pos += 1

        result = "".join(s)
        return result