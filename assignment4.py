num = int(input("enter the number:"))
if num <=0:
 print("enter a positive number ")
else:
 print("multiplication table of",num)
for i in range(1,11):
 print(num,"x",i,"=",num*i)
