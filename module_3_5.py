def get_multiplied_digits(number) :
  str_number = str(number)
  first = int(str_number[0])
  while len(str_number) > 1 :
     return int( first * get_multiplied_digits(int(str_number[1:])))
  else :
    if first == 0 :
      return 1  
    return first
result = get_multiplied_digits(1004030200)
print(result)