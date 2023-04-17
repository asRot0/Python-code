from collections import deque

s = "abcde"
goal = "cdeab"
print(len(s) == len(goal) and s in goal+goal)
# try:
#     ind = s.index(goal[0])
# except:
#     print('no')
#     exit()
#
# print(ind)
# item = deque(s)
# item.rotate(-ind)
# print(''.join(item))
