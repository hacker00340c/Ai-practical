x, y, z, w, v = input("Please enter all marks separated by space: ").split()
print("Please confirm these are the marks : " , x,y,z,w,v)
confirm = input("Yes/No: " )
if confirm == "Yes" :
    A = int(x)
    B = int(y)
    C = int(z)
    D = int(w)
    E = int(v)
    Sum = A + B + C + D + E
    Avg = Sum / 5
    print("AVERAGE MARKS=", Avg)

elif(confirm == "yes"):
    A = int(x)
    B = int(y)
    C = int(z)
    D = int(w)
    E = int(v)
    Sum = A + B + C + D + E
    Avg = Sum / 5
    print("AVERAGE MARKS=", Avg)

else:
    print("Please run the function again")