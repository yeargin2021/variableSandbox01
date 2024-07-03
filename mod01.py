import os
import touch


x = 1

def foo(x):
    return x + 1

print(foo(10))

touch.touch('file'+str(foo(12)))

# def slick():
#
#     crazy = "casanova"+str(foo(x))
#     os.mkdir(crazy)
#
#     # os.close(os.open(crazy, os.O_CREAT))
#
#
# slick()