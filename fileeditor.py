with open('hello.txt','a') as f:
    f.write('Channy \n')
print()
with open('hello.txt','r') as f:
    s = f.read()
    print(s)