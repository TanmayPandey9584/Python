#Remove Duplicate

'''
class Solution:
    def removeDuplicates(self, nums):
        if len(nums)==0:
            print(nums)
        j=0
        for i in range(len(nums)):
            if nums[i]!=nums[j]:
                j+=1
                nums[j]=nums[i]
        return j+1

if __name__=="__main__":
    c=Solution()
    nums=[0,0,1,1,1,2,2,3,3,4]
    c.removeDuplicates(nums)
    c.removeDuplicates([1,1,2])
'''

#Remove Duplicate II
class Solution:
    def removeDuplicates(self, nums):
        if len(nums)==0:
            print(nums)
        j=0

        for i in nums:
            if j<2 or i!=nums[j-2]:
                nums[j]=i
                j+=1
        return j


if __name__=="__main__":
    c=Solution()
    nums= [1,1,1,2,2,3]
    print(nums)
    print(c.removeDuplicates(nums))
    #print(c.removeDuplicates([0,0,1,1,1,1,2,3,3]))
