# Input: num = 58
# Output: "LVIII"
# Explanation: L = 50, V = 5, III = 3.
dict1 = { 1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL',
              50: 'L', 90: 'XC', 100: 'C', 400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'}
integer = int(input("Enter a number: "))
list1 = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

i=0
while i<len(list1):
    if list1[i]!=0:
        rem=integer/list1[i]
        # print(rem)
        if rem!=0:
            for num in range(int(rem)):
                # print(list1[i])
                print(dict1[list1[i]],end="")
        integer=integer%list1[i]
        # print(integer,"integer")
    i+=1


