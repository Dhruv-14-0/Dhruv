# n=5
# for i in range(1,n+1):
#     print(" "*((n+1)-i-1),end="")
#     print("*"*i)


n=5
for i in range(1,n+1):
    for j in range((n+1),0,-1):
        if j>i:
            print(" ",end="")
        else:
            print("*",end="")
    print()    