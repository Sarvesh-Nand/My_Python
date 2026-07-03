from math import sqrt

num = int(input("Enter a number: "))
result = []


# Brute Force

# for i in range(1, num + 1):
#   if num % i == 0:
#     result.append(i)
# print(result)


# Better Approach

# for i in range(1, num//2):
#   if num % i == 0:
#     result.append(i)
# result.append(num)
# print(result)


# Optimal Approach

for i in range(1, int(sqrt(num)) + 1):
  if num % i == 0:
    result.append(i)
    if i != num // i:
      result.append(num // i)
result.sort()
print(result)