class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d={}
        for i in strs:
            c=[0]*26
            for j in i:
                c[ord(j)-ord("a")]+=1
            k=tuple(c)
            if k not in d:
                d[k]=[]
            d[k].append(i)
        return list(d.values())
