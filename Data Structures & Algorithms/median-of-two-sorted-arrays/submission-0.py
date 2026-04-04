class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) < len(nums2):
            nums1, nums2 = nums2, nums1

        l = 0 
        r = len(nums2) - 1
        total = len(nums2) + len(nums1)
        half = total // 2

        while True:
            m = (l + r) // 2
            end_A = half - m - 2

            B_left = nums2[m] if m >= 0 else float("-infinity")
            B_right = nums2[m + 1] if (m + 1) < len(nums2) else float("infinity")
            A_left = nums1[end_A] if end_A >= 0 else float("-infinity")
            A_right = nums1[end_A + 1] if (end_A + 1) < len(nums1) else float("infinity")

            if A_left > B_right:
                l = m + 1
            elif B_left > A_right:
                r = m - 1
            else:
                if total % 2 == 0:
                    return (max(B_left, A_left) + min(B_right, A_right)) / 2
                else:
                    return min(B_right, A_right)
                
        return -1
            






