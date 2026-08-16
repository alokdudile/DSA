# Alok
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = 0
        for i in range(len(digits)):
            num = (num * 10) + digits[i]
        num += 1
        digits = [int(d) for d in str(num)]
        return digits