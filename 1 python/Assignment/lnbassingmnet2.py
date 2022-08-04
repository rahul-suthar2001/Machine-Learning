A = int(input("Enter the value of A : "))
B = int(input("Enter the value of B : "))
C = int(input("Enter the value of C : "))

maximum = max(A, max(B,C))

total_len = A+B+C+(maximum-A)+(maximum-B)+(maximum-C)

print("Total Length : ",total_len)