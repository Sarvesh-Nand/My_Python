num = int(input("Enter a number: "))
while num > 0:
  last_digit = num % 10
  print(last_digit)
  num //= 10
