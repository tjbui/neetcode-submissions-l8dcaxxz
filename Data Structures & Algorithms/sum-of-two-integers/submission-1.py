class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF        # 32 bits of 1s
        max_int = 0x7FFFFFFF     # max positive 32-bit int

        curr_sum = (a ^ b) & mask
        carry = ((a & b) << 1) & mask

        while carry != 0:
            new_sum = (carry ^ curr_sum) & mask
            new_carry = ((curr_sum & carry) << 1) & mask

            curr_sum = new_sum
            carry = new_carry

        return curr_sum if curr_sum <= max_int else ~(curr_sum ^ mask)

# a = 4, b = 7
# a = 0010,
# b = 0111

# 