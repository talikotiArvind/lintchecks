# s = "-H-HH--"
# - -> -
# H -> -H
# - -> -H-
# H -> -HTH
# H -> -HTHH


# # dd = s.split('-')
# # print(dd)
# q = s[0]
# for i in range(1, len(s)+1):
#   q+= i
#   if i == 'H':
    
#     if (s[i-1], s[i+1]) == ('-', '-'):
      



    
# #   if 
# #   if i == 'H':
# #     if (s[i-1], s[i+1]) == ('-', '-'):
      
# #   else:
# #     q+= i

# # # print(s.count('H'))
# # arr = []
# # def check(s):
# #   if len(s) == 1:
# #     return -1
# #   else:
# #     length = len(s)
# #   for i, j in enumerate(s):
# #     if i == 0:
# #       pass

# #     if j == 'H':
# #       if (s[i-1], s[i+1]) == ('-', '-'):

      







# # # ddd = s.replace('-', 'T')

# # # print(ddd)

# # # q = ddd.split('T')
# # # print(q)

def check(a):
  arr = "{0:b}".format(a)
  qqq = [len(i) for i in arr.split('1')]
  if len(qqq) == 2:
    return 0
  else:
    return max(qqq)

print(check(1041))

