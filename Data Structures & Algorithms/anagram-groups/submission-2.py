from collections import defaultdict

def groupAnagrams(strs: list[str]) -> list[list[str]]:
    # 존재하지 않는 키를 조회할 때 자동으로 빈 리스트([])를 생성하는 딕셔너리
    anagram_map = defaultdict(list)
    
    for word in strs:
        # 단어를 알파벳 순으로 정렬한 뒤, 다시 문자열로 합칩니다. ("eat" -> "aet")
        sorted_word = "".join(sorted(word))
        
        # 정렬된 문자열을 Key로 삼아 원본 단어를 추가합니다.
        anagram_map[sorted_word].append(word)
        
    # 딕셔너리의 값(Value)들만 모아서 리스트로 반환합니다.
    return list(anagram_map.values())
