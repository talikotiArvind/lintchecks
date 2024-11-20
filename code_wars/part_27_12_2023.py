# # def strip_comments(strng, markers):
# #     print("Original string")
# #     print(strng)
# #     output = ''
# #     for marker in markers:
# #         output = strng.split(marker)
# #         print(f"output: {output}")
# #     return "".join(output)

# # # print((solution('apples, pears # and bananas\ngrapes\nbananas !apples', ['#', '!']), 'apples, pears\ngrapes\nbananas'))

# # ddd = strip_comments('apples, pears # and bananas\ngrapes\nbananas !apples', ['#', '!'])
# # print("Output string:")
# # print(ddd)

# class User:
#   def __init__(self):
#     self.rank = -8
#     self.progress = 0
  
#   def inc_progress(self, rank):
#     relative_rank = int(rank - self.rank)
#     if (rank > 0 and self.rank < 0) or (rank < 0 and self.rank > 0):
#       relative_rank -= 1
#     match relative_rank:
#       case 0:
#         self.progress += 3
#       case -1:
#         self.progress += 1
#       case w if w <= -2:
#         pass
#       case w if w>= 1:
#         self.progress += 10 * relative_rank * relative_rank
    
#     if self.progress >= 100:
#       self.update_rank()
    
#     if self.rank >= 8:
#       self.progress = 0

#   def update_rank(self):
#     self.progress -= 100
#       self.rank += 1

# def move_zeros(lst):
#     result = [i for i in lst if i!= 0]
#     result.extend([0] * lst.count(0))
#     return result

# print(move_zeros([1, 0, 1, 2, 0, 1, 3]))

# def josephus_survivor(n, k):
#     lst = list(range(1, n+1))
#     copy_lst = lst.copy()
#     while len(copy_lst) != 1:
#         for element in copy_lst:
            
           

# print(josephus_survivor(7, 3))

# def flatten(*x):
#     if len(x) != 0:
#         print(type(x))
#         if type(x) != list:
#             return sum(x, [])
#         else:
#             return list(x)
#     else:
#         return []
    
# print(flatten([1,2],[3,4,5],[6,[7],[[8]]]))


# def luck_check(string):
#     data = [int(i) for i in string]
#     if len(data) % 2 != 0:
#         middle = int((len(data))/2)
#         del data[middle]
#     if sum(data[0:(int(len(data)/2))]) == sum(data[(int(len(data)/2)):]):
#         return True
#     else:
#         return False
    
# print(luck_check('003111'))

# def solution(array_a, array_b):
#     result = list(zip(array_a, array_b))
#     sum = 0
#     for i,j in result:
#         sum += (i - j)**2
#     output = sum/len(result)
#     if output.is_integer():
#         return int(output)
#     else:
#         return output
    
# b1 = [10, 20, 10, 2]
# b2 = [10, 25, 5, -2]

# print(solution(b1, b2))

# def ips_between(start, end):
#     data = list(zip(start.split('.'), end.split('.')))[::-1]
#     output = 0
#     for value  in data:
#         output+= (int(value[1])- int(value[0])) * (256 ** data.index(value))
#     return output

# print(ips_between("10.0.0.10", "10.0.1.0"))

# from itertools import permutations
# def permutations_call(s):
#     return sorted(list(set([''.join(i) for i in permutations([*s])])))
  
# print(permutations_call('dcba'))
def sum_of_squares(n):
    limit_value = int(n ** 0.5)
    output = []
    result = n
    while result != 0:
        var = limit_value * limit_value
        if result >= var:
            output.append(var)
            result-= var
    print(f"Output : {output}")
    return len(output)

print(sum_of_squares(19))