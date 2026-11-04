from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countsMap = defaultdict(int)
        for num in nums:
            countsMap[num] += 1

        buckets = [[] for _ in range(len(nums) + 1)]

        for num, counts in countsMap.items():
            buckets[counts].append(num)

        currCount = len(nums)
        topK = []
        while k > 0:
            currBucket = buckets[currCount]
            if len(currBucket) > 0:
                topK.append(currBucket[-1])
                currBucket.pop()
                k -= 1
            else:
                currCount -= 1

        return topK



# 1, 2, 2, 3, 3, 3, k = 2

# len(nums) = 6
# buckets = [[], [], [], [], [], [], []]

# 