num = int(input("Enter a number: "))
counter = 0
while num > 0:
  last_digit = num % 10
  num //= 10
  counter += 1
print(counter)