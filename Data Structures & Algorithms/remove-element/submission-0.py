class Solution:

    def removeElement(self, nums: List[int], val: int) -> int:
        # 살아남은 원소들이 들어갈 위치를 가리키는 포인터
        pointer = 0

        # 배열을 처음부터 끝까지 탐색
        for i in range(len(nums)):
            # 현재 원소가 지워야 할 값(val)이 아니라면
            if nums[i] != val:
                # pointer가 가리키는 자리에 값을 덮어씌우고
                nums[pointer] = nums[i]
                # 다음 자리를 가리키도록 pointer를 1 증가
                pointer += 1

        # 최종적으로 살아남은 원소의 개수(pointer의 위치)를 반환
        return pointer
