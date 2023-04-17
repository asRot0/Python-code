x = 120

# if -2**31 < num < 2**31:
#     print(True)
# else:
#     print(False)
# print(int(str(num)[1:][::-1]))


x = -abs(int(str(x)[1:][::-1])) if x < 0 else int(str(x)[::-1])
if -2**31 < x < 2**31:
    print(x)
else:
    print(0)
