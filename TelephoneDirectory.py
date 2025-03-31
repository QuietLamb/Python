tele_dic = {'Chinese res':('010-1234'), 
            'Japanese res':('010-2230'), 
            'Western res':('010-3232')}

for k,v in tele_dic.items():
    print(k,":",v)
for k,v in tele_dic.items():
    address = input("Enter address: ")
    review = input("Enter review: ")
    tele_dic[k] = (v,address,review)

for k,v in tele_dic.items():
    print(k,' :',v)