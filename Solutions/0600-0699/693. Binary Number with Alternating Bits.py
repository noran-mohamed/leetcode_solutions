class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        binary_str = format(n, 'b')
        print(binary_str)
        if '11' in binary_str or '00' in binary_str:
            return False
        return True
