

# def add_in_list(arr, d):
#   for i in arr:
#     if d < i:
#       arr.insert(arr.index(i), d)


# def linear(n):
#   arr = []
#   arr.append(1)
#   i = 0
#   while n-1 > 0:
#     y = arr[i] * 2 + 1
#     z = arr[i] * 3 + 1

#     if y < z:
#       arr.add_in_list(arr, y)
#       arr.add_in_list(arr, z)
#     elif y > z:
#       arr.add_in_list(arr, z)
#       arr.add_in_list(arr, y)
#     else:
#       arr.append(y)
#     i += 1
#     n -= 1
  
#   return arr

# print(linear(3))


a = [1, 2, 3]

def check(A):
  output = 1
  for i in set(A):
      if output == i:
          output += 1
      else:
          return output
  return max(A) + 1

print(check(a))
