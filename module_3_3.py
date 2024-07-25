def  print_params(a = 1, b = 'строка', c = True) :
    print(a,b,c)
print_params()
print_params(2,'string')
print_params(b = 25)
print_params(c = [1,2,3])
values_list = [495,'Мосва',7373948]
values_dict = { 'a':495 ,'b':'Moskow', 'c': True}
values_list_2 = [54.32, 'Строка' ]
print_params(*values_list )
print_params(**values_dict)
print_params(*values_list_2, 42)
