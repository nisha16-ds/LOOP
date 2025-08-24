#To print the reverse number
num = int(input("enter the numbers::"))
rev=0

while(num>0):
    digit = num%10     #remainder
    num=num//10      #remove last digit
    rev = rev*10+digit
    print(rev)