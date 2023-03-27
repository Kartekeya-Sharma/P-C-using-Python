sumn = int(input("Enter sum: "))
lis = [i for i in range(0,sumn+1)]
print("Possible combinations of i, j and k are:")
for i in lis:
    for j in lis:
        for k in lis:
            if i+j+k==sumn:
                print(i,j,k)