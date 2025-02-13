
# def median_of_two_sorted_array(nums1, nums2):
#     s = []
#     i = 0
#     j = 0
#     while i < len(nums1) or j < len(nums2):
#         if i < len(nums1) and j < len(nums2):
#             if nums1[i] <= nums2[j]:
#                 s.append(nums1[i])
#                 i += 1
#             else:
#                 s.append(nums2[j])
#                 j += 1
#         elif i < len(nums1):
#             s.append(nums1[i])
#             i += 1
#         else:
#             s.append(nums2[j])
#             j += 1
#     median = s[len(s) // 2] if len(s) % 2 != 0 else (s[len(s) // 2 - 1] + s[len(s) // 2]) / 2
#     return s, float(median)
# def median_of_two_sorted_array(nums1, nums2):
#     s = []
#     i = 0
#     j = 0
#     while i < len(nums1) and j < len(nums2):
#         if nums1[i] <= nums2[j]:
#             s.append(nums1[i])
#             i += 1
#         else:
#             s.append(nums2[j])
#             j += 1
#     while i < len(nums1):
#         s.append(nums1[i])
#         i += 1
#     while j < len(nums2):
#         s.append(nums2[j])
#         j += 1
#     median = s[len(s) // 2] if len(s) % 2 != 0 else (s[len(s) // 2 - 1] + s[len(s) // 2]) / 2
#     return s, float(median)
#
#
# s1 = [1, 3]
# s2 = [2]
# print(median_of_two_sorted_array(s1, s2))
#

# def median_of_two_sorted_array(nums1, nums2):
#     s = []
#     i = 0
#     j = 0
#     k = (len(nums1) + len(nums2)) // 2 + 1
#     while (i < len(nums1) or j < len(nums2)) and len(s) < k:
#         if i < len(nums1) and j < len(nums2):
#             if nums1[i] <= nums2[j]:
#                 s.append(nums1[i])
#                 i += 1
#             else:
#                 s.append(nums2[j])
#                 j += 1
#         elif i < len(nums1):
#             s.append(nums1[i])
#             i += 1
#         else:
#             s.append(nums2[j])
#             j += 1
#     median = s[-1] if (len(nums1) + len(nums2)) % 2 != 0 else (s[-2] + s[-1]) / 2
#     return float(median)
#
#
# s1 = [1, 3]
# s2 = [2]
# print(median_of_two_sorted_array(s1, s2))

def median_of_two_sorted_array(nums1, nums2):
    total = len(nums1) + len(nums2)
    half = total // 2
    a, b = nums1, nums2
    if len(nums2) < len(nums1):
        a, b = b, a
    l, r = 0, len(a) - 1
    while True:
        i = (l + r)//2
        j = half - i - 2
        lefta = a[i] if i >= 0 else float('-infinity')
        righta = a[i+1] if i+1 < len(a) else float('infinity')
        leftb = b[j] if j >= 0 else float('-infinity')
        rightb = b[j+1] if j+1 < len(b) else float('infinity')
        if lefta <= rightb and leftb <= righta:
            # odd case
            if total % 2:   # means total % 2 != 0
                return min(righta, rightb)
            else:
                return (min(righta, rightb) + max(leftb, lefta)) / 2
        if lefta > rightb:
            r -= 1
        else:
            l += 1

s1 = [1, 3]
s2 = [2]
print(median_of_two_sorted_array(s1, s2))
























