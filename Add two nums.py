def addTwoNumbers(l1, l2):
    i=0
    str1=""
    str2=""
    sum=0
    while i<len(l1):
        str1+=str(l1[i])
        i+=1
    k=0
    while k<len(l2):
        str2+=str(l2[k])
        k+=1

    sum=str(int(str1)+int(str2))
    # return type(sum)
    j=0
    l3=[]
    while j<len(sum):
        l3.append(sum[j])
        j+=1
    return l3
l1 = [2,4,3]
l2 = [5,6,4]
print(addTwoNumbers(l1,l2))
        
        