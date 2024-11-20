def nones(itr):
    return [nones(a) if isinstance(a, (list, tuple)) else None for a in itr]


def same_structure_as(a, b):
    return nones(a) == nones(b) if type(a) == type(b) else False

# ----------------------------------------------------------------------------------

a = [1,2,3,4,5,6,7]

# print(a.index(2))


# def josephus(xs, k):
#     i, ys = 0, []
#     while len(xs) > 0:
#         i = (i + k - 1) % len(xs)
#         ys.append(xs.pop(i))
#     return ys

# print(josephus(a, 3))

formula = "Mg(OH)2"

def parse_molecule (formula):
    if ('(' or '[') in formula:
        print("Yes")
        data = formula.split('(')
        print(data)
    else:
        print("No")

parse_molecule(formula)