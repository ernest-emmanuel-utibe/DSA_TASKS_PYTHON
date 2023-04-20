#        Given two sorted arrays nums1 and nums2 of size m and n respectively,
#        return the median of the two sorted arrays.The overall run time complexity should be O(log (m+n)).

def find_median_sorted(nums1, nums2):


n1 = len(nums1)
n2 = len(nums2)
addedNumbers = n1 + n2
new_arr = [addedNumbers]

i , j , k = 3
