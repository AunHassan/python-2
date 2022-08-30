list1 = (input("enter space sepearted elments").split(" "))
# list = [1,4,3,2,6,9,8,5,7]
print((list1))
list = sorted(list1)
search = int(input(":"))
# list = input("enter space sepearted elments")
start_ind = 0
end_ind = len(list)
mid = (start_ind+end_ind)//2
print("start index =",start_ind,"end index =",end_ind,"middle index =",mid,"middle element =",list[mid])
for i in range(len(list)):
    if int(list[mid]) == search:
        print(mid)
        break
    elif int(list[mid]) < search:
        start_ind = mid + 1
        # mid = (start_ind+end_ind)//2
    elif int(list[mid]) > search:
        end_ind = mid - 1
    mid = (start_ind+end_ind)//2
    print("start index =",start_ind,"end index =",end_ind,"middle index =",mid,"middle element =",list[mid])



    # mid = len(list)//2
    # if list[mid] == search:
    #     print(i)
    # elif mid >= search:
    #     start_ind = mid + 1
    # elif mid == search:
    #     end_ind = mid - 1
    
