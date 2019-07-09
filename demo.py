c=0
def one(n):
    print(n)
    for i in range(0, 7):
        two(i)
        c+=1
        print("value of c: "+c)

def two(m):
    print(m)
    for j in range(0,2):
        one(j)
        c+=1
        print("value of c: "+c)        

one(1)        