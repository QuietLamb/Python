s_list = ['abc', 'bcd', 'bcdefg', 'abba', 'cddc', 'opq']

for item in s_list:
    item  = len(item)
    print(item, end=", ")
    
short = len(s_list[0])

for search in s_list:
    current = len(search)
    if current>short:
        long = current
        longest = long
        print("\n")
        print(longest)


