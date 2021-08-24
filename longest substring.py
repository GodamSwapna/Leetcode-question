# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
s="abcabcbb"
str1=""
i=0
while i<len(s):
    if s[i] not in str1:
        str1+=s[i]
    i+=1
print(len(str1))
