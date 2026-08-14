#Alok
class Solution:
    def reverse(self, x: int) -> int:
        if x > 0:
            sign = 1
        else:
            sign = -1
        x = abs(x)
        revnum = 0
        while x > 0:
            lastdigit = x % 10
            x = int(x / 10)
            revnum = (revnum * 10) + lastdigit
        revnum *= sign
        if revnum < -2**31 or revnum > 2**31 - 1:
            return 0
        return revnum 