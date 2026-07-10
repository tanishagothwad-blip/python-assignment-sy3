num=float(input("Enter a number:"))
if num>0:
    print("The number is positive")
elif num<0:
    print("The number is negative")
else:
    print("The number is zero")


marks=float(input("Enter your marks:"))
if marks>=90:
    print("Grade: A")
elif marks>=80:
    print("Grade: B")
elif marks>=60:
    print("Grade: C ")
else:
    print("Fail")

ch=input("Enter a character:").lower()
if ch in 'aeiou':
    print("Vowel")
else:
    print("Consonant")