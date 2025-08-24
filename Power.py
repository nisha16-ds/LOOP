#. You are given two integers A and B. You have to find the value of A^B.
A = int(input("enter the number A:"))
B = int(input("enter the number B:"))

result = 1
count = 0

while count < B:
    result = result * A   
    count = count + 1     

print(A, "^", B, "=", result)





