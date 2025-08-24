#To print the sum of digit like (INPUT=1234,OUTPUT=10)

num= int(input("enter the numbers::"))
sum=0
while(num>0):
    digit = num%10
    sum += digit
    num= num//10
    print(sum)