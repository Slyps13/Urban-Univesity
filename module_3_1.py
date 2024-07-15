calls = 0
def count_calls() :
  global calls
  calls += 1
  return calls
def string_info(string) :
  count_calls()
  s = []
  s.append (len(string))
  s.append (string.upper())
  s.append (string.lower())
  return s
print(string_info('Hello '))
def  is_contains (string ,list_to_search) :
  count_calls()
  for i in range (len(list_to_search)) :
    if list_to_search[i].upper() == string.upper() :
      return True
  return False
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)
