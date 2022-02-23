#1st sub-division
d = [[1, "Abc", 90],
     [2, "Def", 95],
     [3, "Ghi", 85]]

print("{:<8} {:<15} {:<10}".format('Roll_No', 'Name', 'Marks'))

for v in d:
    Roll_No, Name,Marks = v
    print("{:<8} {:<15} {:<10}".format(Roll_No,Name, Marks))

#2nd sub-division
print('\r')
for n in range(len(d[2])):
    print(d[1] [n] , end="\t")