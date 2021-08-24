input="3322251"
i=0
str1=""
str2=""
while i<len(input):
    c=input.count(input[i])
    if input[i] not in str1:
        str1+=input[i]
        if input[i]=="1":
            str2=str2+"One"+","+str(c)+"+"
            print(str2)
        if input[i]=="2":
            str2=str2+"Two"+","+str(c)+"+"
            print(str2)
        if input[i]=="3":
            str2=str2+"Three"+","+str(c)+"+"
            print(str2)
        if input[i]=="4":
            str2=str2+"Four"+","+str(c)+"+"
            print(str2)
        if input[i]=="5":
            str2=str2+"Five"+","+str(c)+"+"
            print(str2)
        if input[i]=="6":
            str2=str2+"Six"+","+str(c)+"+"
            print(str2)
        if input[i]=="7":
            str2=str2+"Seven"+","+str(c)+"+"
            print(str2)
        if input[i]=="8":
            str2=str2+"Eight"+","+str(c)+"+"
            print(str2)
        if input[i]=="9":
            str2=str2+"Nine"+","+str(c)+"+"
            print(str2)
        if input[i]=="0":
            str2=str2+"Zero"+","+str(c)+"+"
            print(str2)
    i+=1
print(str2)















def convert(s,b): 
    # num = num * 10 + (ord(i) - 48) 
    print("s",(ord(s)-48)*(ord(b)-48)) 
s = "2"
b="3"
convert(s,b) 