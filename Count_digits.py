#Take an integer N as input and print the count of digits of that number.

num = int(input("Enter a no. : "))
original = num 
digits=0
while(num!=0):
    num//=10 
    digits=digits+1
print(digits)