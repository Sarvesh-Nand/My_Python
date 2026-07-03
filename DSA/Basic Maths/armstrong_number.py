num = int(input("Enter a number: "))
original_num = num
armstrong = 0
while num > 0:
  last_digit = num % 10
  armstrong += last_digit ** 3
  num //= 10
if original_num == armstrong:
  print("Armstrong Number")
else:
  print("Not an armstrong number")