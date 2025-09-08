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
        # map = {n: i for i, n in enumerate(nums1)}
        # res = [-1] * len(nums1)

        # for i in range(len(nums2)):
        #     if nums2[i] not in map:
        #         continue
        #     for j in range(i+1, len(nums2)):
        #         if nums2[j] > nums2[i]:
        #             idx = map[nums2[i]]
        #             res[idx] = nums2[j]
        #             break
        # return res

        # print(map)
        # print(res)

        """
        Optimal Solution: Implementing Monotonic Stack
        Time : O(n+m)
        Space: O(m)
        """
        # Initializing the hashmap
        map = {n:i for i, n in enumerate(nums1)}
        # Initializing a result array of size equal to nums1 with all element as -1
        res = [-1] * len(nums1)
        # Empty stack for push pop operations
        stack = []

        for i in range(len(nums2)):
            curr = nums2[i]
            # While stack is non-empty and curr is greater than top element of stack
            while stack and curr > stack[-1]:
                # We pop the top element
                val = stack.pop() # New greater element is found 
                idx = map[val] # Find the index of that element using the hashmap
                res[idx] = curr # Place that element in the result
            
            # If current element also exists in the map(map of nums1)
            if curr in map:
                # Simply push that element in the stack
                stack.append(curr)
        return res