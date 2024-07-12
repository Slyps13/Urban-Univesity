numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
Primes = []
not_primes = []
is_prime = True
for i  in range(len (numbers) -1 ) :
  for j  in range(len(Primes)) :
    if (numbers[i+1] % Primes[j] == 0) :
      is_prime = False
      break
    else :
      is_prime = True
      
  if is_prime :
    Primes.append(numbers[i+1])
  else :
    not_primes.append(numbers[i+1])
   
print('Not primes :' , not_primes) 
print('Pimes :' , Primes)