# Given the string representations of two integers, return the string representation of the sum of those integers.

# For example:

# sumStrings('1','2') // => '3'
# A string representation of an integer will contain no characters besides the ten numerals "0" to "9".

# I have removed the use of BigInteger and BigDecimal in java

# Python: your solution need to work with huge numbers (about a milion digits), converting to int will not work.

# import ctypes
# def sum_strings(x, y):
#     w = ctypes.c_uint64(int(x, 16) + int(y, 16))
#     print(int(x, 16) , int(y, 16))
#     return(str(w.value))

# z = sum_strings('123','456')
# print(z, type(z))


# from itertools import combinations, permutations
# def next_smaller(n):
#     words = [(''.join(p)) for p in permutations(str(n), len(str(n)))]
#     print(words)
#     q = {}
#     for i in words:
#         q[i] = int(i) - int(n)
#     z = [int(i) for i in q.values()]
#     x = [i for i in z if i < 0]
#     print(q)
#     if len(x) == 0:
#         return -1
#     for key, value in q.items():
#         if max(x) == int(value) and len(key) == len(str(n)):
#             return key
#     return -1
        
# print(next_smaller(1027))

# def rgb(r,g,b):
#   data = ''
#   for i in [r,g,b]:
#     if i < 1:
#       data += '00'
#     elif i > 255:
#       data += 'FF'
#     else:
#         data += "{:02x}".format(i).upper()
#   return data

# print(rgb(255,255,255))

def count_ones(left, right):
    # Your code here!
    count = 0
    for i in range(left, right+1):
        iter_count = [int(d) for d in "{0:b}".format(i)]
        count += sum(iter_count)
    return count

print(count_ones(12,29))