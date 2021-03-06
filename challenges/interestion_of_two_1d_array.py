"""
## Intersection of Two Arrays II

Link: https://leetcode.com/problems/intersection-of-two-arrays-ii/

Given two arrays, write a function to compute their intersection.

Example 1:

```
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
```

Example 2:

```
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
```

Note: Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.
"""

from collections import defaultdict


def intersect(nums1, nums2):
    """Alternative Method Using Defaultdict"""
    if not nums1 or not nums2:
        return []

    _min = min(nums1, nums2)
    _max = max(nums1, nums2)

    counter = defaultdict(int)
    for i in range(0, len(_min)):
        counter[_min[i]] = 1

    for i in range(0, len(_max)):
        if _max[i] in counter:
            counter[_max[i]] += 1

    return [k for k, v in counter.items() if v > 1]


nums1 = [4, 9, 5]
nums2 = [9, 4, 9, 8, 4]

intersect(nums1, nums2)

from collections import Counter


def intersect(nums1, nums2):
    if not nums1 or not nums2:
        return []

    # save in a multiset the smallest
    counter = Counter(nums1)
    print(counter)

    # find matches, removing from counter when found
    matches = []
    for num in max(nums1, nums2):
        if counter[num] > 0:
            matches.append(num)
            counter[num] -= 1
    return matches


nums1 = [4, 9, 5]
nums2 = [9, 4, 9, 8, 4]

intersect(nums1, nums2)
