class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sorting the array in place
        nums.sort()
        n = len(nums)
        answer = []

        for i in range(n):
            # if the number at ith position is positive 
            # and the array is sorted, the sum can never be == 0
            if nums[i] > 0:
                break
            # If the current number in i is equal to the 
            # previous number, we continue so that for loop 
            # increments i in the next iteration
            elif i > 0 and nums[i] == nums[i-1]:
                continue

            lo, hi = i+1, n-1
            while lo < hi:
                sum = nums[i] + nums[lo] + nums[hi]
                if sum == 0:
                    # append the list in the answer array if 
                    # sum == 0
                    answer.append([nums[i], nums[lo], nums[hi]])
                    # increment & decrement lo and hi respectively
                    lo, hi = lo + 1, hi - 1
                    # while lo & hi are still in bounds and the 
                    # current number at low is equal to the previous 
                    # lo, we increment the lo pointer again
                    while lo < hi and nums[lo] == nums[lo - 1]:
                        lo += 1
                    # Same condition for hi pointer as well
                    while lo < hi and nums[hi] == nums[hi + 1]:
                        hi -= 1
                # if sum is negative, we need to shift the lo
                # pointer towards right to make the sum == 0
                elif sum < 0:
                    lo += 1
                # Also if sum is positive, we need to shift the hi
                # pointer towards left to make the sum == 0
                else:
                    hi -= 1
        return answer
                    