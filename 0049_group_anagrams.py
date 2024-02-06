class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        common = {}
        for string in strs:
            sort = ''.join(sorted(string))
            if sort not in common:
                common[sort] = [string]
            else:
                common[sort].append(string)
        return[value for value in common.values()]
