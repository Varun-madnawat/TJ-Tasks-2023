# Q1 Given two numbers a and b as interval range, the task is to find the prime numbers in between this interval.
# Examples:

# Input : a = 1, b = 10 Output : 2, 3, 5, 7 Input : a = 10, b = 20 Output : 11, 13, 17, 19

#Solution: 


# def prime(a,b):
#     for i in range(a,b):
#         if i > 1:
#             for j in range(2, int(i/2)+1):
#                 if (i % j) == 0:
#                     break
#             else:
#                 print(i,end=',')
# a = int(input("Enter first number of range: "))
# b = int(input("Enter last number of range: "))

# prime(a,b)

# -----------------------------------------------------------------------------------------------------------------------------------


# Q2 Given a non-negative integer n. The problem is to reverse the bits of n and print the number obtained after reversing the bits. Note that the actual binary representation of the number is being considered for reversing the bits, no leadings 0’s are being considered. Examples :
# Input : 11 Output : 13 Explanation: (11)10 = (1011)2. After reversing the bits we get: (1101)2 = (13)10.

# Input : 10 Output : 5 Explanation : (10)10 = (1010)2. After reversing the bits we get: (0101)2 = (101)2

#Solution: 

# n = int(input("Enter a number: "))
# b = ''
# while (n != 0):
#     r = n%2
#     b = b + str(r)
#     n = n//2
#     s = b[::-1]

# print("Binary transformation of given number is : ", s)
# print("Reverse of the binary number: ",b)

# z = int(b)
# dn = 0
# i = 0
# while (z != 0):
#     decimal = z % 10
#     dn = dn + decimal * pow(2, i)
    
#     z = z // 10
#     i = i+1

# print("output: ",dn)

# -----------------------------------------------------------------------------------------------------------------------------------