class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = {}
        for num in nums:
            result[num] = result.get(num,0)
            result[num]+=1
        # print(result)    
        vals = {k: v for k, v in sorted(result.items(), key=lambda item: item[1],reverse=True)}
        # print(vals)
        return list(vals.keys())[:k]
        
        # for ky,v in result.items():
        #     if v > k:
        #         vals.append(ky)
        # return vals if len(vals) > 0 else  nums