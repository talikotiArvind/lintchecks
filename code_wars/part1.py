def rgb(r, g, b):
    a = []
    for i in [r,g,b]:
        if i > 255:
            a.append(255)
        elif i < 0:
            a.append(0)
        else:
            a.append(i)
    return "{:02x}{:02x}{:02x}".format(a[0],a[1],a[2]).upper()

# print(rgb(255,300,255))

#-------------------------------------------------------------------------#
'''
The Hashtag Generator

The marketing team is spending way too much time typing in hashtags.
Let's help them with our own Hashtag Generator!

Here's the deal:

It must start with a hashtag (#).
All words must have their first letter capitalized.
If the final result is longer than 140 chars it must return false.
If the input or the result is an empty string it must return false.
Examples

" Hello there thanks for trying my Kata"  =>  "#HelloThereThanksForTryingMyKata"
"    Hello     World   "                  =>  "#HelloWorld"
""                                        =>  false
'''

def hastag_gen(data):
    # d = " Hello there thanks for trying my Kata"
    val = data.split(" ")
    s = []
    for i in val:
        if i != '':
            s.append(str(i).capitalize())
    ddd = "".join(s)
    if 0 < len(ddd) <= 140:
        return("#" + ddd)
    else:
        return False
    
# print(hastag_gen(""))

#-----------------------------------------------------------------------------#

'''
Data Reverse
A stream of data is received and needs to be reversed.

Each segment is 8 bits long, meaning the order of these segments needs to be reversed, for example:

11111111  00000000  00001111  10101010
 (byte1)   (byte2)   (byte3)   (byte4)

should become

10101010  00001111  00000000  11111111
 (byte4)   (byte3)   (byte2)   (byte1)

input in form of stream
'''

def data_reverse(data):
    z = []
    val = [data[i:i+8] for i in range(0,len(data),8)][::-1]
    # print(val)
    for i in val:
        # print("i : {}".format(i[::-1]))
        z = z + i[::-1]
    return(z)

my_list = [1,2,3,4,5,6,7,8,9]
d = [1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,1,0,1,0,1,0]
# print(my_list)
# print(data_reverse(d))

#-------------------------------------------------------------------------------------
'''your task is to create all permutations of a non-empty input string and remove duplicates, if present.

Create as many "shufflings" as you can!

With input 'a':
Your function should return: ['a']

With input 'ab':
Your function should return ['ab', 'ba']

With input 'abc':
Your function should return ['abc','acb','bac','bca','cab','cba']

With input 'aabb':
Your function should return ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa']

'''
from itertools import permutations

def permutationss(s):
    w = list(permutations([*s]))
    z = []
    for i in w:
        z.append("".join(i))
    sss = list(set(z))
    return sss

# print(permutationss('aabb'))
# Didnt work

#-----------------------------------------------------------------------------------------
'''Human Readable Time
Write a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable format (HH:MM:SS)

HH = hours, padded to 2 digits, range: 00 - 99
MM = minutes, padded to 2 digits, range: 00 - 59
SS = seconds, padded to 2 digits, range: 00 - 59
The maximum time never exceeds 359999 (99:59:59)

You can find some examples in the test fixtures.'''

def make_readable(seconds):
    hr, buffer = int(seconds / 3600), seconds % 3600
    min, sec = int(buffer / 60), buffer % 60
    return("{:02d}:{:02d}:{:02d}".format(hr, min, sec))

# print(make_readable(60))

import dis
print(dis.dis(make_readable))