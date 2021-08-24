def marged_list(lists):
    i=0
    new_l=[]
    while i<len(lists):
        new_l+=lists[i]
        i+=1
    return new_l
lists = [[1,4,5],[1,3,4],[2,6]]

def sorted_list(list1):
    j=0
    while j<len(list1):
        k=0
        while k<len(list1):
            if list1[j]<list1[k]:
                list1[j],list1[k]=list1[k],list1[j]
            k+=1
        j+=1
    return list1
input=marged_list(lists)
print(sorted_list(input))
# Output: [1,1,2,3,4,4,5,6]