f = open('testfile.txt','r')
su = 0
for i in range(5):
    n = int(f.readline())
    su = su+n
print('sum is: ',su)