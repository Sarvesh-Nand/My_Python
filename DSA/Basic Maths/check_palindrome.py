def reverse_num(num:int):
  reversed_num = 0
  while num > 0:
    last_digit = num % 10
    reversed_num = reversed_num * 10 + last_digit
    num //= 10
  return reversed_num

num = int(input("Enter a number: "))
reversed_number = reverse_num(num)

if num == reversed_number:
  print("It is a palindrome")
else:
  print("Not a palindrome")