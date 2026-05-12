class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans=""
        n=min(len(i) for i in strs)
        for i in range(n):
            target = strs[0][i]
            for j in range(1, len(strs)):
                if strs[j][i]!=target:
                    return ans
            ans+=target
        return ans