def twoSum(nums,target):
    i=0
    while i<len(nums):
        j=0
        while j<len(nums):
            if nums[i]+nums[j]==target:
                return [nums.index(nums[i]),nums.index(nums[j])]
            j+=1
        i+=1
num=9
list1=[2,7,11,15]
print(twoSum(list1,num))
    
        