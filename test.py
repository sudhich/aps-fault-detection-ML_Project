import os,sys
var=sys
try:

    a = 1/0

except Exception as e:
    _, _, exc_tb = var.exc_info()
print(_, _, exc_tb)