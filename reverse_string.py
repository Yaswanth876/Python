str1=input("enter a string:")
str2=''
index=-1
for i in str1:
    str2+=str1[index]
    index-=1
print("the given string ={} \n the reversed string ={}".format(str1,str2))
