from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # 후보(candidate)와 카운터(count) 초기화
        candidate = None
        count = 0
        
        for num in nums:
            # 카운트가 0이 되면 현재 숫자를 새로운 후보로 지정
            if count == 0:
                candidate = num
            
            # 현재 숫자가 후보와 같으면 표를 더하고, 다르면 표를 깎음
            count += (1 if num == candidate else -1)
            
        return candidate
