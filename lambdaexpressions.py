# lambda expressions
# lambda param: action(param)
from functools import reduce
my_list = [1,2,3]


def multiply_by2(item):
    return item % 2 != 0

def accumulator(acc, item):
    print(acc, item)
    return acc + item

print(list(map(multiply_by2, my_list)))
print(my_list)



# lambda expressions(don't need to create a new function)

from functools import reduce
my_list = [1,2,3]


def accumulator(acc, item):
    print(acc, item)
    return acc + item

print(list(map(lambda item: item*2, my_list)))
print(my_list)




# another example lambda expressions

from functools import reduce

my_list = [1,2,3]



def accumulator(acc, item):
    print(acc, item)
    return acc + item

print(list(filter(lambda item: item % 2 != 0, my_list)))
print(my_list)


# another example lambda expressions

from functools import reduce

my_list = [1,2,3]


def accumulator(acc, item):
    print(acc, item)
    return acc + item

print(reduce(lambda acc, item: acc + item, my_list))
print(my_list)


