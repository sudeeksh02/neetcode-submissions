class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left=0
        right=len(nums)-1
        if len(nums)==1:
            if nums[0]==target:
                return 0
            else:
                return -1
        while left<right:
            mid=left+(right-left)//2
            if target==nums[mid]:
                return mid
            if nums[mid]>nums[right]:
                if target>=nums[left] and target<nums[mid]:
                    right=mid
                else:
                    left=mid+1
            else:
                if target>nums[mid] and target<=nums[right]:
                    left=mid+1
                else:
                    right=mid
            if left==right:
                if nums[left]==target:
                    return left
                else:
                    return -1
        return -1