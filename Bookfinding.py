def valid_date(date):
    days = [31,29,31,30,31,30,31,31,30,31,30,31]
    sherlock_series = [1887,1890,1892,1894,1901,1905,1915,1917,1927]
    splitted = date.split('.')
    year = int(splitted[0])
    month = int(splitted[1])
    day = int(splitted[2])
    is_sherlock_book_yr = lambda x:x in sherlock_series

    if not is_sherlock_book_yr(year):
        print('this is not a publication year')
        return False 
    if month < 1 or month >12:
        print('ivalid month')
        return False
    if day < 1 or day > days[month-1]:
        print('invalid day')
        return False
    return True
user = input("E: ")
print(valid_date(user))