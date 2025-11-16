def fizzbuzz(n):
  if n % 3 == 0 and n % 5 == 0:
    print('FizzBuzz')
  elif n % 3 == 0:
    print('Fizz')
  elif n % 5 == 0:
    print('Buzz')
  else:
    print(n)


str_list = []
for _ in range(3):
  str_list.append(input())

for str_input in str_list:
  if str_input.isdigit():
    fizzbuzz(int(str_input) + (3 - str_list.index(str_input)))
    break
