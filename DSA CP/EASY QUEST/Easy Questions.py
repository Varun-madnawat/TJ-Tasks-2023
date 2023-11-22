# 1.Write a program to reverse an array or string.
# Examples:
# Input : arr[] = {1, 2, 3} Output : arr[] = {3, 2, 1}
# Input : arr[] = {4, 5, 1, 2} Output : arr[] = {2, 1, 5, 4}

#Solution: I used basic knowlwdge of for loop and reverse indexing to reverse the string.

# arr = [1,2,3]
# rra = []
# for i in range(len(arr), 0, -1):
#     rra.append(i)
# print("Given array  is: ", arr)
# print("Reversed array is: ", rra)


# -----------------------------------------------------------------------------------------------------------------------------------


# 2. Given an array of N integers, and an integer K, the task is to find the number of pairs of integers in the array whose sum is equal to K.
# Examples:

# Input: arr[] = {1, 5, 7, -1}, K = 6 Output: 2 Explanation: Pairs with sum 6 are (1, 5) and (7, -1).

# Input: arr[] = {1, 5, 7, -1, 5}, K = 6 Output: 3 Explanation: Pairs with sum 6 are (1, 5), (7, -1) & (1, 5).

# Input: arr[] = {1, 1, 1, 1}, K = 2 Output: 6 Explanation: Pairs with sum 2 are (1, 1), (1, 1), (1, 1), (1, 1), (1, 1).

# Input: arr[] = {10, 12, 10, 15, -1, 7, 6, 5, 4, 2, 1, 1, 1}, K = 11 Output: 9 Explanation: Pairs with sum 11 are (10, 1), (10, 1), (10, 1), (12, -1), (10, 1), (10, 1), (10, 1), (7, 4), (6, 5).


#Solution: I used double for loop for double indexing and stored the output in a list(o) and then stored the list(o) in another list(out) and found its length to find desired output. 

# n = [10, 12, 10, 15, -1, 7, 6, 5, 4, 2, 1, 1, 1]
# k = 11
# out = []
# for i in range(len(n)):
#     for j in range(i+1):
#         if (n[i] + n[j] == k):
#             o = []
#             o.append(n[i])
#             o.append(n[j])
#             out.append(o)
# print(out)
# s = len(out)
# print(s)

# -----------------------------------------------------------------------------------------------------------------------------------

# Q3 Given an array arr[] of size N-1 with integers in the range of [1, N], the task is to find the missing number from the first N integers.
# Note: There are no duplicates in the list.

# Examples:

# Input: arr[] = {1, 2, 4, 6, 3, 7, 8} Output: 5 Explanation: Here the size of the array is 7, so the range will be [1, 8]. The missing number between 1 to 8 is 5

# Input: arr[] = {1, 2, 3, 5}, N = 5 Output: 4 Explanation: Here the size of the array is 4, so the range will be [1, 5]


#Solution: I Used membership operator not in to find the missing number in array.

# arr = [1, 2, 3, 5]
# m =  max(arr)
# for i in range(1,m+1):
#     if (i not in arr):
#         print("output: ", i)

# -----------------------------------------------------------------------------------------------------------------------------------