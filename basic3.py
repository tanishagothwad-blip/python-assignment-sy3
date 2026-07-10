num=int(input("Enter number:"))
for i in range(2,num):
    if num%i==0:
        print("Not prime")
        break
else:
    print("Prime")


num=int(input("Enter number:"))
rev=int(str(num)[::-1])
if num==rev:
    print("Palindrome")
else:
    print("Not palindrome")