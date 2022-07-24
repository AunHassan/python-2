# stage o
nr = int(input("enter number of row in a matrix you want:"))
nc = int(input("enter number of col in a matrix you want:"))

# make list
m = []
# start a loop
for r in range(nr):
    row = []
    for c in range(nc):
# take input
        i = int(input(f"enter values of {r+1}.{c+1}:"))
        row.append(i)
    m.append(row)
for r in range(nr):
    for c in range(nc):
        print("%7.3f" % m[r][c],end = " ")
    print()
# print(m)

    # for r in range(nr):
    #     for c in range(nc):
    #          print("%7.3f" % m[r][c],end = " ")
    #     print()



pr = int(input("input pivot row :"))
pc = int(input("input pivot column :"))
pr = int(pr)-1
pc = int(pc)-1
print("pivot row you selected is :",pr)
print("pivot col you selected is :",pc)
while (pr >=0 and pc >= 0):
    pv = m[pr][pc]
    print("pivot value is:",pv)
    # make 1
    for c in range(nc):
        m[pr][c] = m[pr][c]/pv
    print("after making 1 ")
    for r in range(nr):
        for c in range(nc):
            print("%7.3f" % m[r][c],end = " ")
            # print()
        print()
    for r in range(nr):
        if r == pr:
            continue
        make0 = m[r][pc]
        for c in range(nc):
            m[r][c] = m[r][c] - make0*m[pr][c]
        print("after making 0")
        for r in range(nr):
            for c in range(nc):
                print("%7.3f" % m[r][c],end = " ")
            #  print()
            print()

    pr = input("input pivot row :")
    pc = input("input pivot column :")
    pr = int(pr)-1
    pc = int(pc)-1
else:
    print("wrong index")