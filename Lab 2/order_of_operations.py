exp1 = 5 // 9 * (53 - 32)
print(exp1)

# In exp1, the operation 53-32 is calculated first as it's within the parenthesis and Python follows PEMDAS left to right.
# 5 // 9 is then evaluated after the parentheses function and goes from left to right.
# 5 // 9 returns a value of 0 since it's the floor division operator and is rounding down to the closest integer
# When 21 from the right side parenthesis is multiplied by 5 // 9 which has a value of 0, we get 0 * 21 = 0

exp2 = (53 - 32) * 5 // 9
print(exp2)

# In exp2, we continue to evaluate 53-32 first since it's in parentheses which gives us a value of 21 still.
# This value is then multiplied by 5 since it's first in the order left to right and * and // have the same level of priority in order of operations
# This then becomes 105 // 9. 9*11 = 99 which is the closest integer we can get to 105 since 9*12 would be 108.
# The floor division operator just rounds down to 11 since 105/9 is 11.66 and cannot be a float basically.