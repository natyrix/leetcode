class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}
        for st in strs:
            sortStr = sorted(st)
            sortst = "".join(sortStr)
            keys = result.keys()
            if sortst in keys:
                result[sortst].append(st)
            else:
                result[sortst] = [st]
        return result.values()
                
            