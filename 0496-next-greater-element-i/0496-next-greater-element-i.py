class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        Brute Force Solution:
        ▷ Time: O(n*m); Notice it's not O(n²) because we're not finding 
        the next greater for every element in nums2 but insted in nums1.
        ▷ Space: O(m); because we're implementing a hashmap for len(nums1)
        and we're also building the output
        """
        # Initializing a hashmap
        map = {n: i for i, n in enumerate(nums1)}
        res = [-1] * len(nums1)

        for i in range(len(nums2)):
            if nums2[i] not in map:
                continue
            for j in range(i+1, len(nums2)):
                if nums2[j] > nums2[i]:
                    idx = map[nums2[i]]
                    res[idx] = nums2[j]
                    break
        return res

        # print(map)
        # print(res)