class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        vals = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        sums = 0
        i = 0
        for i in range(len(s)):
            if i + 1 < len(s) and vals[s[i]] < vals[s[i+1]]:
                sums -= vals[s[i]]
            else:
                sums += vals[s[i]]
        return sums
        
    def checkAndReturnVal(self, i,j=None):
        vals = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        keys = vals.keys()
        if j is None:
            return vals[i], False
        s = "{}{}".format(i,j)
        if s == "LV" or s == "XV" :
            return vals[i], False
        else:
            if keys.index(i) < keys.index(j):
                return vals[i]-vals[j], True
            else:
                return vals[i], False
        