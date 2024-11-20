# from itertools import permutations

# # val = 123
# # d = [*str(val)]
# # # print(d)
# # a = permutations(d)
# # # print(list(a))
# # dd = []
# # for i in a:
# #     # print(i)
# #     dd.append(int(''.join([str(elem) for elem in i])))
# #     # dd.append(''.join(list(i)))
              
# # print(dd)

# def data(val):
#     dd, ss = [], {}
#     for i in permutations([*str(val)]):
#         dd.append(int(''.join([str(elem) for elem in i])))
#     for w in dd:
#         ss[w] = val-w
#     ss.pop(val)
#     print(ss)
#     return [k for k,v in ss.items() if v == max(list(ss.values()))][0]


# print(data(2017))


def summ(d):
    s = [int(w) for w in str(abs(d))]
    return sum(s)

print(summ(-9525))
        