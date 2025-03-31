# Q1
# n_list = [1,2,3,4,5,6,7,8,9,10]
# even_list = []
# for i in filter(lambda x : x%2 == 0, n_list):
#     even_list.append(i)
# print(even_list, end=' ')


# Q2
# n_list = [1,2,3,4,5,6,7,8,9,10]
# even_list = list(filter(lambda x : x%2 == 0, n_list))
# print(even_list,end=' ')


# Q3
a_list = ['a','b','c','d']
to_list = map(lambda x: x.upper(), a_list)
upper_list = list(to_list)
print(upper_list)

# Q4
# import functools

# n = range(1,101)

# result = functools.reduce(lambda x,y: x+y,n)
# print(result)