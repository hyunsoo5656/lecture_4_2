list_a = [10,20 ,30]
list_b = [10,20 ,30]

if list_a is list_b:
    print('list_a is list_b')
else:
    print('list_a is not list_b')

print('list_a 는 {}'.format(id(list_a)))
print('list_b 는 {}'.format(id(list_b)))

num_a = {"a","b"}
num_b = {"a","b"}

def is_func_1():
    print("Hello")

def is_func_2():
    print("Hello")

if type(is_func_1()) == type(is_func_2()):
    print('type(is_func_1) is type(is_func_2())')
else:
    print('num_a is not num_b')

if num_a is num_b:
    print('num_a is num_b')
else:
    print('num_a is not num_b')


if num_a is not num_b:
    print('num_a is num_b')
else:
    print('num_a is not num_b')


if list_a == list_b:
    print('list_a is list_b')
else:
    print('list_a is not list_b')