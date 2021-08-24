# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.

nums1=[1,2,5]
nums2 = [3,4,6]

num3=nums1+nums2
print(num3)
i=0
while i<len(num3):
    j=0
    while j<len(num3):
        if num3[j]>num3[i]:
            num3[i],num3[j]=num3[j],num3[i]
        j+=1
    i+=1
print(num3)
if len(num3)%2!=0:
    index=len(num3)/2
    if index<0:
        index+=0
    print("median of list",num3[int(index)])
else:
    index1=len(num3)/2
    median1=(num3[int(index1-1)]+num3[int(index1)])/2
    print(median1)


# print("Merged list ",num3)