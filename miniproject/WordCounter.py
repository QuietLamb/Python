file = open('/Users/anbschool0008/VSCODE/miniproject/text.txt', 'r+')
content = file.read()

text = content.split()

result = {}
for i in text:
    if i in result:
        result[i] += 1
    else:
        result[i] = 1
print(result)
