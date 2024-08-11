data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]
sum_all = 0
def calculate_structure_sum(data_structure) :
  global sum_all
  l = len(data_structure)
  for i in range(l)  :
    if isinstance(data_structure[i],str) :
       sum_all += len(data_structure[i])
    if isinstance(data_structure[i],int) :
       sum_all += data_structure[i]
    elif isinstance(data_structure[i],list) :
       calculate_structure_sum(data_structure[i])
    elif isinstance(data_structure[i],dict):
       for key,value in data_structure[i].items():
         if not isinstance(value,int) :
           sum_all += len(key) + len(value)
         else :
           sum_all += value+len(key)
    if isinstance(data_structure[i],tuple) or isinstance(data_structure[i],set):
      calculate_structure_sum(list(data_structure[i]))

  return sum_all    
result = calculate_structure_sum(data_structure)
print(result)
