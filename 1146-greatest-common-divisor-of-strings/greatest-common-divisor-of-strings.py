class Solution(object):
    def gcdOfStrings(self, str1, str2):
        if str2 in str1:
            import fractions
            result = ""


            N = fractions.gcd(len(str1), len(str2))
            candidate = str1[:N]

            s1 = candidate * (len(str1) // len(candidate))
            s2 = candidate * (len(str2) // len(candidate))

            if s1 == str1 and s2 == str2:
                return candidate
            else:
                return ""
        elif str1 in str2:
            import fractions
            result = ""


            N = fractions.gcd(len(str1), len(str2))
            candidate = str1[:N]

            s1 = candidate * (len(str1) // len(candidate))
            s2 = candidate * (len(str2) // len(candidate))

            if s1 == str1 and s2 == str2:
                return candidate
            else:
                return ""
        else:
            return ""
