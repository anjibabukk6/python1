counter = 0
# while counter<10:
# 	counter += 3
# 	print(counter)


#1.


# l=[]
# for i in range(2000, 3201):
#  if (i%7==0) and (i%5!=0):
# 	 l.append(str(i))
# print(sep=','.join(l))
# print(l)
# print(len(l))
#
# #
#
# 2.
# def fact(x):
#     if x == 0:
#         return 1
#     return x * fact(x - 1)
#
#
# x = int(input())
# print(fact(x))
# from audioop import reverse
#
# import self as self


#
#
#
# 3.
# n = int(input())
# d = dict()
# for i in range(1, n + 1):
#     d[i] = i * i
# print(d)

#

#4.
# values = input()
# l = values.split(',')
# t = tuple(l)
# print(l)
# print(t)


#  5.
# class InputOutString(object):
#     def __init__(self):
#         self.s = ""
#
#     def getString(self):
#         self.s = input()
#
#     def printString(self):
#         print(self.s.upper())
#
#
# strObj = InputOutString()
# strObj.getString()
# strObj.printString()


# #6.
# import math
#
# c = 50
# h = 30
# value = []
# items = [x for x in input().split(',')]
# for d in items:
#     value.append(str(int(round(math.sqrt(2 * c * float(d) / h)))))
# print(sep=','.join(value))
# print(value)



#  #.7
# input_str = input()
# dimensions = [int(x) for x in input_str.split(',')]
# rowNum = dimensions[0]
# colNum = dimensions[1]
# multilist = [[0 for col in range(colNum)] for row in range(rowNum)]
# for row in range(rowNum):
#     for col in range(colNum):
#       multilist[row][col] = row*col
#
# print(multilist)



#  8.
# items = [x for x in input().split(',')]
# items.sort()
# print(sep="".join(items))
# print(items)

# 9.
# lines = []
# while True:
#     s = input()
#     if s:
#         lines.append(s.upper())
#     else:
#         break;
# for sentence in lines:
#  print(sentence)


# 10.
# s = input()
# words = [word for word in s.split(" ")]
# print(" ".join(sorted(list(set(words)))))
# hello world and practice makes perfect and hello world again



# 11.
# value = []
# items = [x for x in input().split(',')]
# for p in items:
#     intp = int(p, 2)
#     if not intp % 5:
#         value.append(p)
# print(','.join(value))
# 0100,0011,1010,1001



# 12.
# values = []
# for i in range(1000, 3001):
#     s = str(i)
#     if (int(s[0]) % 2 == 0) and (int(s[1]) % 2 == 0) and (int(s[2]) % 2 == 0) and (int(s[3]) % 2 == 0):
#         values.append(s)
# print(",".join(values))

# 13.
# s = input()
# d={"DIGITS":0, "LETTERS":0}
# for c in s:
#     if c.isdigit():
#         d["DIGITS"] += 1
#     elif c.isalpha():
#         d["LETTERS"] += 1
#     else:
#         pass
# print("LETTERS", d["LETTERS"])
# print("DIGITS", d["DIGITS"])
#