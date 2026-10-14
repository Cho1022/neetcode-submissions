class MyHashSet:

    def __init__(self):
        # key의 범위인 0 ~ 1,000,000을 커버하기 위해 크기 1,000,001 배열 생성
        self.set_array = [False] * 1000001

    def add(self, key: int) -> None:
        self.set_array[key] = True

    def remove(self, key: int) -> None:
        self.set_array[key] = False

    def contains(self, key: int) -> bool:
        return self.set_array[key]
