class Solution:
    def removeDuplicates(self, n: list[int]) -> int:
        n[:] = sorted(list(set(n)))
        
            