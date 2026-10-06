class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs: 
            return "" #리스트가 비여 있다면 -> "" 

        #for i 는 한문자씩 뽑고 range는 0~n-1까지, len은 길이 == 해당 문자의 인덱스 길이
        for i in range(len(strs[0])):
            # strs[0] = "flower" strs[0][0] = "f" 이다.
            char = strs[0][i]

            # 문자열 두번째랑 비교해야지 
            for s in strs[1:]:
                if i == len(s) or s[i] != char: 
                    return strs[0][:i]
        return strs[0]
