a=int(input())
b=int(input())
def find_strong_numbers_in_range(a,b):
    for i in range(a,b+1):
        y=0
        num=i
        while i>0:
            x=1
            c=i%10
            i=i//10
            for k in range(1,c+1):
                x=x*k
            y=x+y
        if y==num:
            print(y)
find_strong_numbers_in_range(a,b)
