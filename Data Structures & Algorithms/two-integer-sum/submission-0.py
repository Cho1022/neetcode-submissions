def twoSum(nums: list[int], target: int) -> list[int]:
    # 숫자와 해당 숫자의 인덱스를 저장할 딕셔너리
    num_to_index = {}
    
    for i, num in enumerate(nums):
        # target을 만들기 위해 필요한 나머지 숫자
        complement = target - num
        
        # 그 숫자가 이미 딕셔너리에 있다면 정답 반환
        if complement in num_to_index:
            # 문제 조건에 따라 작은 인덱스부터 반환 (기존 인덱스가 무조건 작음)
            return [num_to_index[complement], i]
        
        # 현재 숫자와 인덱스를 딕셔너리에 기록
        num_to_index[num] = i