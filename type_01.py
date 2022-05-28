for num in range(1, 101):
    string = ''

    # ここから記述
    if num % 15 == 0: #15の倍数の場合
      print('FizzBuzz')
      continue
    elif num % 3 == 0: #3の倍数の場合
      print('Fizz')
      continue
    elif num % 5 == 0: #5の倍数の場合
      print('Buzz')
      continue
    string += str(num) #それ以外の倍数の場合
    # ここまで記述

    print(string)
