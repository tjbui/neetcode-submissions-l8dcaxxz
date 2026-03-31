class Solution {
public:
    uint32_t reverseBits(uint32_t n) {
        uint32_t result = 0;
        for (int i = 0; i < 32; i++) {
            result |= (((n >> i) & 1) << (31 - i));
        }

        return result;
    }
};

// 0000 0010 0110

// 000000000001

// 0110 0100 0000