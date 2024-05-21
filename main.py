import utils.math_functions as mf

mf.add(1, 2)
mf.subtract(1, 2)

import getpass

pwd = getpass.getpass(prompt='Enter the password')
if pwd == 'Admin':
    print('Unlock!')
else:
    print('You entered wrong password')