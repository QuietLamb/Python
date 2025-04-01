a = input('Enter words: ')
a = list(a)
b = []
for i in a:
    b.append(i)
a.reverse()
if a == b:
    print('Palindrome')
else:
    print('Not Palindrome')
