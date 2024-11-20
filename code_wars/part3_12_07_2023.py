# def valid_ISBN10(isbn): 
#     data, data2, sum = [*isbn], [], 0
#     for value in data:
#         if value == 'X':
#             data2.append(10)
#         elif (value.isdigit()):
#             data2.append(int(value))
#     print(data2)
#     for key, value in enumerate(data2):
#         sum += (key + 1) * value
#     return (sum % 11 == 0)

# num = '1112223339'
# num = '048665088X'
# num = 'XXXXXXXXXX'
# num = '1293'

# print(valid_ISBN10(num))

# def between(a,b):
#     # good luck
#     return list(range(a,b+1))

# print(between(-2,2))


def ip_to_num(ip):
    data = [int(i) for i in ip.split(".")]
    return int.from_bytes(data, "big")

def num_to_ip(num):
    value = [ str(i) for i in list(num.to_bytes(4, byteorder = 'big'))]
    return ".".join(value)

val = ip_to_num("192.168.1.1")

ip = num_to_ip(val)
print(ip)