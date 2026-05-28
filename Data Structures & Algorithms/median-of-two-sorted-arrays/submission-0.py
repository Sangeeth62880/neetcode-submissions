class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A,B = nums1,nums2
        if len(A) > len(B):
            A,B = B,A
        m,n = len(A),len(B)
        total = m+n
        half = total//2
        l,r = 0,m-1
        while True:
            i = (l+r)//2
            j = half - i - 2
            A_left = A[i] if i >= 0 else float('-inf')
            A_right = A[i+1] if i+1 < m else float('inf')
            B_left = B[j] if j >= 0 else float('-inf')
            B_right = B[j+1] if j+1 < n else float('inf')
            if A_left <= B_right and B_left <= A_right:
                if total %2:
                    return min(A_right,B_right)
                return (max(A_left,B_left)+min(A_right,B_right))/2
            elif A_left > B_right:
                r = i - 1
            else:
                l = i + 1
