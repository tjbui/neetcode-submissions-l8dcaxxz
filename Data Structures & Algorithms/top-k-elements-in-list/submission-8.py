from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        for i in nums:
            counts[i] += 1

        buckets = [[] for _ in range(len(nums) + 1)]

        for num, count in counts.items():
            buckets[count].append(num)

        result = []
        curr = len(nums)
        while k > 0:
            if len(buckets[curr]) != 0:
                result.append(buckets[curr].pop())
                k -= 1
                continue
            else:
                curr -= 1

        return result

    # k = 3
    # 3, 2, 1

