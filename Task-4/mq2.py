s = input("string: \n")
size = len(s)
opt = ''
for i in range(size):
    if i%2 == 0:
        opt = opt + s[i]
    else:
        pass
print(opt)