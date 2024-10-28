from fake_math import Divide as F_Divide
from true_math import Divide as T_Divide
result1 = F_Divide(69, 3)
result2 = F_Divide(3, 0)
result3 = T_Divide(49, 7)
result4 = T_Divide(15, 0)
print(result1)
print(result2)
print(result3)
print(result4)
