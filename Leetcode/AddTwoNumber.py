'''
class Solution:
    def isPalindrome(self, x: int) -> bool:
        import numpy as np
        x=np.array(x)
        a=x[::-1]
        if np.array_equal(a,x) == "true":
            return np.array_equal(a,x)
        else:
            return "false"

x=121
print(Solution.isPalindrome(x=121))
'''

'''
import numpy as np
a=input("enter the palidrome")
t=np.array([int(digit) for digit in a])
array=t[::-1]
print(np.array_equal(array,t))
'''
x=int(input(""))

import numpy as np

t = np.array([digit for digit in str(x)])
a = t[::-1]
if np.array_equal(a, t) is True:
    print(np.array_equal(a, t))
else:
    print(False)