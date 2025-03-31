a = (('211101', 'David', '99999'), 
      ('211102', 'John', '88888'), 
      ('211103', 'Jane', '77777'))

id = {}

for i in a:
    stuId = i[0]
    name = i[1]
    phone = i[2]
    id[stuId] = [name,phone]

for k,v in id.items():
    print(k,":",v)

n = input("Enter ID: ")

if n in id:
    print("Name: ",id[n][0])
    print("Phone Number: ",id[n][1])
    