from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagram_map = defaultdict(list)
        
        for word in strs:
            # 1. 단어를 정렬하여 key로 사용
            sorted_word = "".join(sorted(word))
            
            # 2. 딕셔너리에 추가
            anagram_map[sorted_word].append(word)
            
        # 3. 결과 반환
        return list(anagram_map.values())
