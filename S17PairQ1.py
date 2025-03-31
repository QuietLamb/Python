input = input("Enter three number: ")
a, b, c = map(int,input.split())

def mean3(a,b,c):
    result = (a+b+c)/3
    return result
def max3(a,b,c):
    if a>b and a>c:
        return a
    elif c>b and c>a:
        return c
    else:
        return b
def min3(a,b,c):
    if a<b and a<c:
        return a
    elif c<b and c<a:
        return c
    else:
        return b


showresultmean3 = mean3(a,b,c)
showresultmax3 = max3(a,b,c)
showresultmin3 = min3(a,b,c)
print('The average of',a,b,c,'is = ',showresultmean3)
print('The max of',a,b,c,'is = ',showresultmax3)
print('The min of',a,b,c,'is = ',showresultmin3)