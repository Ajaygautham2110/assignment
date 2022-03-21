print('1. \n')
import os
file_path = os.path.splitext('file.txt')

print(file_path[1],'\n')

print('2.')
import timeit

start = timeit.timeit()
print("\n","33*33")
end = timeit.timeit()
print("\n",'time taken to calculate the eq is ',"\n",end - start)



print('3.')
comb_list = dict(zip([1,2,3,4,5],['a','b','c','d','e']))
print("\n", comb_list,'\n')


print('4.')
class num:
    def __init__(self, num):
        self.num = num
x = num(1)
print (type(x).__name__)
